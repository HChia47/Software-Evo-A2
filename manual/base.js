function checkIfEnoughPoints(listOfPositionsScored) {
    let amount = 0;
    for (let i = 0; i < listOfPositionsScored.length; ++i) {
        if (listOfPositionsScored[i] = 1) {
            amount = amount + 5;
        }
        else {
            amount++;
        }
    }
    if (amount > 20) {
        return true;
    }
    else {
        return false;
    }
}