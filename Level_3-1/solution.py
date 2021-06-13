import numpy as np
from fractions import Fraction

def solution(m):
  """Takes a matrix (list of lists) of nonnegative integers - an absorbing Markov chain - and
  returns a list of integers - the probability of each terminal state as numerators + the common
  denominator."""
  if len(m) <= 1:
    return [1, 1]
  terminal_rows_i = get_terminal_rows_i(m)
  ls_gis = calc_geom_inf_sum(matrix_int_to_percentage(m))[0]
  return get_res_with_lcd([perc for i, perc in enumerate(ls_gis) if i in terminal_rows_i])

def get_terminal_rows_i(m):
  return [row_i for row_i in range(len(m)) if sum(m[row_i]) == 0]

def matrix_int_to_percentage(m):
  """Converts matrix of integers to a matrix of percentages for each state."""
  return [row if sum(row) == 0 else [n / float(sum(row)) for n in row] for row in m]

def calc_geom_inf_sum(m):
  """Calculates the geometric infinite sum of matrices: S = (I - m) ^ -1"""
  return np.linalg.inv(np.subtract(np.identity(len(m)), m))

def get_res_with_lcd(ls_percentages):
  """Turns percentages into fractions and finds least common denominator."""
  ls_fractions = [Fraction(perc).limit_denominator() for perc in ls_percentages]
  numers = [fraction.numerator for fraction in ls_fractions]
  denoms = [fraction.denominator for fraction in ls_fractions]
  lcd = np.lcm.reduce(denoms)
  return [n * int(lcd / denoms[i]) for i, n in enumerate(numers)] + [lcd]
