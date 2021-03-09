function victoryChecker(listOfPositionsScored) {
    var score = 0;
    for (let c = 0; c < listOfPositionsScored.length; ++c) {
        if (listOfPositionsScored[c] = 1) {
            score = score + 5;
        }
        else {
            score++;
        }
    }
    if (score > 20) {
        return true;
    }
    else {
        return false;
    }
}