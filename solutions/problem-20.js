let sum = 0;

for (let i = 1; i <= 5; i++) {
    let number = Number(prompt(`أدخل الرقم ${i}:`));
    sum += number;
}

let average = sum / 5;

console.log("المتوسط الحسابي = " + average);
alert("المتوسط الحسابي = " + average);