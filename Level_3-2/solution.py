def solution(n):
  """Takes a positive integer as a string and returns the minimum number of operations needed to
  transform the number to 1."""
  if (len(n) <= 309):
    n = int(n)
    count = 0
    while n > 1:
      if (n % 2) == 0:
        n /= 2
      elif (n & 3) == 1 or n == 3:
        n -= 1
      else:
        n += 1
      count += 1
    return count
