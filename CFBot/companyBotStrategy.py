def companyBotStrategy(trainingData):
    answers = [trainingData[i][0] for i in range(len(trainingData)) if trainingData[i][1] == 1]
    return (sum(answers))/len(answers) if len(answers) > 0 else 0
