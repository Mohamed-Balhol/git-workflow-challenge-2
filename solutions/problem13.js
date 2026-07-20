function calculateFactorial() {
    let input = prompt("Enter a positive integer:");
    let num = Number(input);

    if (isNaN(num) || num < 0) {
        alert("Enter a valid positive integer!");
        return; 
    }

    let result = 1;
    for (let i = 1; i <= num; i++) {
        result = result * i; 
    }

    console.log("Entered Number: " + num);
    console.log("Factorial of the number (" + num + "!) is: " + result);
}