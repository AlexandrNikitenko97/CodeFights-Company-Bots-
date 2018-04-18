def incorrectPasscodeAttempts(passcode, attempts):
    success = [i == passcode for i in attempts]
    falseInRow = 0
    maxFalseInRow = [0]
    for i in range(len(success)):
        if success[i] is False:
            falseInRow += 1
            maxFalseInRow.append(falseInRow)
        else:
            falseInRow = 0
    return True if max(maxFalseInRow) >= 10 else False
