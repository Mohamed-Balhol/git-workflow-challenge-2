let year = Number(prompt("أدخل السنة:"));

if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
    alert(year + " سنة كبيسة");
} else {
    alert(year + " سنة بسيطة");
}