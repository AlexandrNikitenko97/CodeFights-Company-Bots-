def taskMaker(source, challengeId):
    pattern = r"//DB " + str(challengeId) + "//"
    newSource = []
    for line in source:
        if "//DB" in line:
            if pattern in line:
                newSource[-1] = line.replace(pattern, "")
        else:
            newSource.append(line)
    return newSource
