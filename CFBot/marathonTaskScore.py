# Super Ugly Solution
def marathonTaskScore(marathonLength, maxScore, submissions, successfulSubmissionTime):
    penaltyScore = ((submissions - 1) if submissions > 1 else 0 ) * 10
    timeScore = maxScore if successfulSubmissionTime <= 1 and submissions == 1 else successfulSubmissionTime * (maxScore / 2) * (1 / marathonLength) 
    return maxScore if (penaltyScore == 0 and timeScore == maxScore) else (0 if successfulSubmissionTime < 0 else (maxScore/2 if (maxScore - timeScore - penaltyScore) < maxScore/2 else (maxScore - timeScore - penaltyScore)))



# Readable solution
def marathonTaskScore(marathonLength, maxScore, submissions, successfulSubmissionTime):
    if submissions > 1:
        penaltyScore = (submissions - 1) * 10
    else:
        penaltyScore = 0
    
    if successfulSubmissionTime <= 1 and submissions == 1:
        timeScore = maxScore
    else:
        timeScore = successfulSubmissionTime * (maxScore / 2) * (1 / marathonLength)
    
    if penaltyScore == 0 and timeScore == maxScore:
        return maxScore
    else:
        if successfulSubmissionTime >= 0:
            if (maxScore - timeScore - penaltyScore) <= maxScore/2:
                return maxScore/2
            else:
                return (maxScore - timeScore - penaltyScore)
        else:
            return 0

    
