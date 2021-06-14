def solution(M, F):
  """Takes quantities (strings) of needed Mach and Facula bombs and returns (string) the fewest
  number of generations (replication cycles) needed to reach those quantities or 'impossible'."""
  M, F = int(M), int(F)
  if (0 < M <= 10 ** 50) and (0 < F <= 10 ** 50):
    count = 0
    while min(M, F) != 1:
      if max(M, F) % min(M, F) == 0:
        return "impossible"
      count += max(M, F) / min(M, F)
      (M, F) = (max(M, F) % min(M, F), min(M, F))
    return str(count + max(M, F) - 1)
