import re
from collections import defaultdict


def solution(plaintext):
  """Takes a string (uppercase and lowercase letters + spaces) and returns a string of 1's and 0's
  representing the bumps and absence of bumps (braille) in the input string"""
  def check_input(input):
    sanitized_input = input.strip()
    words = sanitized_input.split()
    for word in words:
      if word.isalpha() == False:
        return False
    return True

  if check_input(plaintext) == False:
    return

  braille_by_alpha = get_translation_dict()

  braille_translation = ""
  for letter in plaintext:
    if letter.isupper():
      braille_translation += braille_by_alpha.get("-uppercase")
      letter = letter.lower()
    braille_translation += braille_by_alpha.get(letter)
  return braille_translation


ALPHA = "The quick brown fox jumps over the lazy dog"
BRAILLE = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"

def get_translation_dict():
  ls_braille_letters = re.findall('......', BRAILLE)

  braille_by_alpha = defaultdict(str)
  braille_by_alpha["-uppercase"] = "000001"

  j = 0
  for letter in ALPHA:
    if letter.isupper():
      letter = letter.lower()
      j += 1
    braille_by_alpha[letter] = ls_braille_letters[j]
    j += 1

  return braille_by_alpha