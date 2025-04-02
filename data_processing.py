# data_processing.py
import numpy as np
from scipy import interpolate
import io
import pandas as pd


class Spectrum:
    def __init__(self):
        self.name = ''
        self.energy = []
        self.counts = []
        self.interp = []
        self.size = 0
        self.average = 0
        self.angle_size = 0

    def get_size(self):
        self.size = len(self.energy)
        self.angle_size = len(self.counts[0]) if self.counts else 0

    def get_average(self):
        if self.counts:
            self.average = np.mean(self.counts)

    def get_inter(self):
        for iAn in range(self.angle_size):
            counts_iAn = [self.counts[iEn][iAn] for iEn in range(self.size)]
            self.interp.append(interpolate.interp1d(
                self.energy, counts_iAn, kind='slinear'))


def load_data(files, traduzir):
    sum_scan = None
    for file in files:
        if file.size == 0:
            raise ValueError(traduzir("erro_arquivo_vazio"))
        scan = np.loadtxt(file, delimiter=None, skiprows=1)
        if scan.ndim != 2 or scan.shape[1] < 2:
            raise ValueError(traduzir("erro_formato_arquivo"))
        if sum_scan is None:
            sum_scan = scan
        else:
            if sum_scan.shape != scan.shape:
                raise ValueError(traduzir("erro_tamanho_arquivos"))
            sum_scan += scan
    sum_scan[:, 0] /= len(files)
    return sum_scan


def read_file(file, traduzir):
    exp = Spectrum()
    content = file.read().decode('utf-8').splitlines()
    if len(content) < 10:
        raise ValueError(traduzir("erro_arquivo_curto"))
    for row in content:
        thisrow = row.split()
        if len(thisrow) < 2:
            raise ValueError(traduzir("erro_colunas"))
        try:
            energy = float(thisrow[0])
            counts = [float(c) for c in thisrow[1:]]
        except ValueError:
            raise ValueError(traduzir("erro_valores_numericos"))
        exp.energy.append(energy)
        exp.counts.append(counts)
    if exp.energy and exp.energy[0] > exp.energy[-1]:
        exp.energy.reverse()
        exp.counts.reverse()
    exp.get_size()
    return exp


def angle_sum(exp, exp_angle_min, exp_dangle, exp_new_angle_min, exp_new_angle_max):
    new_exp = Spectrum()
    new_exp.energy = exp.energy
    for iEn in range(exp.size):
        counts_sum = 0
        for iAn in range(len(exp.counts[0])):
            angle = iAn * exp_dangle + exp_angle_min
            if exp_new_angle_min <= angle < exp_new_angle_max:
                counts_sum += exp.counts[iEn][iAn]
        new_exp.counts.append([counts_sum])
    new_exp.get_size()
    return new_exp


def rebine(exp, exp_new_denergy):
    new_exp = Spectrum()
    nEn = int((max(exp.energy) - min(exp.energy)) / exp_new_denergy) + 1
    jEn = jEn0 = 0
    for iEn in range(nEn):
        energy = (iEn + 0.5) * exp_new_denergy + min(exp.energy)
        counts = [0 for _ in range(exp.angle_size)]
        while jEn < exp.size and exp.energy[jEn] < energy + exp_new_denergy / 2:
            if jEn == exp.size - 1:
                denergy_j = exp.energy[jEn] - exp.energy[jEn - 1]
            elif jEn > 0:
                denergy_j = min(
                    exp.energy[jEn] - exp.energy[jEn - 1], exp.energy[jEn + 1] - exp.energy[jEn])
            else:
                denergy_j = exp.energy[jEn + 1] - exp.energy[jEn]
            for iAn in range(exp.angle_size):
                counts[iAn] += exp.counts[jEn][iAn] / denergy_j
            jEn += 1
        if jEn - jEn0 > 0:
            for iAn in range(exp.angle_size):
                counts[iAn] = counts[iAn] / (jEn - jEn0) * exp_new_denergy
        new_exp.energy.append(energy)
        new_exp.counts.append(counts)
        jEn0 = jEn
    new_exp.get_size()
    return new_exp


def export_spectrum(spec):
    output = io.StringIO()
    for iEn in range(spec.size):
        line = f"{spec.energy[iEn]}\t" + \
            "\t".join(map(str, spec.counts[iEn])) + "\n"
        output.write(line)
    return output.getvalue()


def load_spectrum_file(file):

    content = file.read().decode('utf-8')
    df = pd.read_csv(io.StringIO(content), sep='\t', header=None)
    df.columns = ['energy', 'count']
    return df
