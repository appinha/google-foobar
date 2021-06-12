from solution import solution

if __name__ == '__main__':
  for input in range(1, 30):
    print("-> input:    {}".format(input))
    print("-> solution: {}\n".format(solution(input)))

  input = 10
  print("-> input:    {}".format(input))
  print("-> solution: {}\n".format(solution(input)))

  input = 143
  print("-> input:    {}".format(input))
  print("-> solution: {}\n".format(solution(input)))
