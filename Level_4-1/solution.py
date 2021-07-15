from itertools import combinations

def solution(num_buns, num_required):
  """Given the number of bunnies available and the number of locks required to open a work room,
  returns a specification of how to distribute the keys such that any num_required bunnies can open
  the locks, but no group of (num_required - 1) bunnies can."""
  if 1 <= num_buns <= 9 and 0 <= num_required <= 9:
    copies_per_key = num_buns - (num_required - 1)
    bunnies_combinations = list(combinations(range(num_buns), copies_per_key))
    return [
        [key for key, bunnies in enumerate(bunnies_combinations) if bunny in bunnies]
        for bunny in range(num_buns)
    ]
