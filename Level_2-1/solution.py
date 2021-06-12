def solution(total_lambs):
  """Gets the integer number of LAMBs to divide and returns an integer which represents the
  difference between the minimum and maximum number of henchmen who can share the LAMBs."""
  if total_lambs < 1 or total_lambs >= 10 ** 9:
    return
  return stingy(total_lambs) - generous(total_lambs)

def generous(total_lambs):
  henchmen = [1]
  while total_lambs > 0:
    total_lambs -= henchmen[-1]
    if total_lambs < 2 * henchmen[-1]:
      break
    henchmen.append(2 * henchmen[-1])
  return len(henchmen)

def stingy(total_lambs):
  if total_lambs == 1:
    return 1
  if total_lambs == 2:
    return 2
  lambs_count = [1, 1]
  while True:
    lambs_count.append(lambs_count[-1] + lambs_count[-2])
    if sum(lambs_count) > total_lambs:
      break
  return len(lambs_count) - 1