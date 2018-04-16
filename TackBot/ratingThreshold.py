def ratingThreshold(threshold, ratings):
    return [i for i in range(len(ratings)) if (sum(ratings[i])/len(ratings[i])) < threshold]
