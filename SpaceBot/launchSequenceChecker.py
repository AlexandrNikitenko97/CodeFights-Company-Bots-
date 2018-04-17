def launchSequenceChecker(systemNames, stepNumbers):
    matched = {}
    result = []
    for i in range(len(systemNames)):
        if systemNames[i] not in matched:
            matched[systemNames[i]] = [stepNumbers[i]]
        else:
            matched[systemNames[i]].append(stepNumbers[i])
    for value in matched.values():
        if len(value) == 1:
            result.append(True)
        else:
            for i in range(len(value)-1):
                if value[i] >= value[i+1]:
                    result.append(False)
                    break
            else:
                result.append(True)
    return True if sum(result) == len(matched) else False
        
