def taskMaker(source, challengeId):
  template = ('//DB ' + str(challengeId) + '//')
  newSource = []
  neededLine = ''
  for i in source:
    if ('//DB' not in i):
      newSource.append(i)
    else:
      if template in i:
        newSource[-1] = i.replace(template, '')
  return newSource
