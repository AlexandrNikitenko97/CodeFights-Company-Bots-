def allianceHelp(t, allianceSize):
    percent = int(t * 0.1)
    if percent < 60:
        percent = 60
    boost = 0
    for i in range(10):
        if i >= allianceSize:
            break
        boost += percent
    print(boost)
    return 0 if t-boost < 0 else t-boost
