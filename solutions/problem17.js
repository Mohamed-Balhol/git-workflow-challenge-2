function checkPrime() {
    let input = prompt("Enter a number to check if it is prime:");
    let num = Number(input);

    if (isNaN(num) || num <= 1) {
        alert("Enter a valid integer greater than 1!");
        return;
    }

    let isPrime = true;

    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            isPrime = false;
            break;
        }
    }

    console.log("Checked Number: " + num);
    
    if (isPrime) {
        console.log("This number is a PRIME number!");
        
    } else {
        console.log("This number is not a prime number!");
       
    }
}