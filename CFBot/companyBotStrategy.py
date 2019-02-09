def companyBotStrategy(trainingData):
    answers = [trainingData[i][0] for i in range(len(trainingData)) if trainingData[i][1] == 1]
    return (sum(answers))/len(answers) if len(answers) > 0 else 0


# more readable variant
def companyBotStrategy(trainingData):
    divider = correct = 0
    for i in trainingData:
        if i[1] == 1:
            correct += i[0]
            divider += 1
    return 0.0 if divider == 0 else correct/divider
            
