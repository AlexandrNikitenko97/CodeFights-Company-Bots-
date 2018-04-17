from collections import Counter

def packetDescrambler(seq, fragmentData, n):
  if list(set(seq)) != list(range(len(set(seq)))):
    return ''
  
  mass = {}
  message = ''
  
  for i in range(len(seq)):
    if seq[i] not in mass:
      mass[seq[i]] = [fragmentData[i]]
    else:
      mass[seq[i]].append(fragmentData[i])
      
  uniqueSeq = list(set(seq))
  
  if '#' not in mass[uniqueSeq[-1]]:
    return ''
  else:
    if mass[uniqueSeq[-1]].count('#') <= n/2:
      return ''
  
  for i in uniqueSeq:
    if len(mass[i]) <= n/2 or len(mass[i]) > n:
      return ''
    if len(set(mass[i])) == 1:
      message += list(set(mass[i]))[0]
    else: 
      elements = Counter(mass[i])
      maxElem = max(elements.values())
      if maxElem <= n/2:
        return ''
      for k, v in elements.items():
        if v == maxElem:
          message += k
          break
      
  return message   
