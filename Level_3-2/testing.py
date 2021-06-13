from solution import solution

if __name__ == '__main__':
  for n in range(3, 17):
    print("-> input:    {}".format(n))
    print("-> solution: {}\n".format(solution(str(n))))