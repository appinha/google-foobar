def solution(x, y):
  """Returns worker ID of bunny at location (x, y)."""
  if (1 <= x <= 100000) and (1 <= y <= 100000):
    return str(lazy_caterer(x - 1, lazy_caterer(y - 1, 1, 1), y + 1))

def lazy_caterer(n, start, step):
  sequence = [start]
  while n:
    sequence.append(sequence[-1] + step)
    step += 1
    n -= 1
  return sequence[-1]
