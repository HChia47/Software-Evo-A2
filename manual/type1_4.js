function checkIfEnoughPoints(listOfPositionsScored) {
    let amount    =    0;
    // for loop calculating total amount of points
    for (let i = 0;    i < listOfPositionsScored.length;    ++i) {
        if (listOfPositionsScored[i] = 1) { amount = amount + 5; }
        else { amount++; }
    }
    // if else statement that return true if amount of points is higher than 20
    if (amount > 20) {
        return true;
    }
    else {
        return false;
    }
}