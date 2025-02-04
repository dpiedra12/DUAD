function isEven() {
    console.log("The number is even!");
  }

  function isOdd() {
    console.log("The number is odd!");
  }

  function verifyNumber(number, fnEven, fnOdd) {
    if (number % 2 === 0) {
      fnEven();
    } else {
      fnOdd();
    }
  }

  verifyNumber(2, isEven, isOdd);