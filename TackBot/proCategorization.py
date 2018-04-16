def proCategorization(pros, preferences):
    result = []
    categorizations = {}
    uniquePreferences = []
    for i in preferences:
        for j in i:
            if j not in uniquePreferences:
                uniquePreferences.append(j)
    uniquePreferences = sorted(uniquePreferences)
    for i in range(len(pros)):
        categorizations[pros[i]] = preferences[i]
    for i in uniquePreferences:
        customers = []
        for k, v in categorizations.items():
            if i in v:
                customers.append(k)                
        result.append([[i], sorted(customers)])
    return result
    
