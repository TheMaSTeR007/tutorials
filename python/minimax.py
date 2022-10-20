def maxPlayer(args):
    childList = []
    for i in args:
        if len(i) != 1:
            first = i[0]
            last = i[-1]
            maxScoreList.append(first)
            maxScoreList.append(last)
            childList.extend([i[1:], i[:len(i) - 1]])
        else:
            first = i[0]
            maxScoreList.append(first)
    if childList:
        # if list is not empty calling min function
        minPlayer(childList)
    else:
        return 0


def minPlayer(args):
    childList = []

    for i in args:
        if len(i) != 1:
            first = i[0]
            last = i[-1]
            minScoreList.append(first)
            minScoreList.append(last)
            childList.extend([i[1:], i[:len(i) - 1]])
        else:
            first = i[0]
            minScoreList.append(first)
    if childList:
        # if list is not empty calling max function
        maxPlayer(childList)
    else:
        return 0


def checkMaxWinningGame(maxScore, minScore):
    if maxScore > minScore:
        return True
    elif minScore > maxScore:
        return False
    else:
        return "Game Tie"


if __name__ == "__main__":
    maxScore = 0
    minScore = 0
    maxScoreList = []
    minScoreList = []

    # input list
    inp = [[1, 2, 5, 2]]

    # max starting the game
    maxPlayer(inp)
    for i in maxScoreList:
        maxScore += i
    for j in minScoreList:
        minScore += j
    print("Score of max: ", maxScore)
    print("Score of min: ", minScore)
    print(checkMaxWinningGame(maxScore, minScore))
