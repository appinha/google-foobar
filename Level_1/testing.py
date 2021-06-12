from solution import solution


if __name__ == '__main__':
  ls_inputs = ["code", "Braille", "The quick brown fox jumps over the lazy dog"]
  ls_solutions = [
    "100100101010100110100010",
    "000001110000111010100000010100111000111000100010",
    "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
  ]

  for i, input in enumerate(ls_inputs):
    print("-> input:    {}".format(input))
    my_solution = solution(input)
    print("-> solution: {}".format(my_solution))
    check = "PASS" if my_solution == ls_solutions[i] else "FAIL"
    print("=> {}\n".format(check))