 function countVowels() {

            let word = prompt("Enter a word to count its vowels");

            if (word !== null && word !== "") {
                
                const vowels = "aeiouAEIOU";
                let counter = 0;

                for (let i = 0; i < word.length; i++) {
                    
                    if (vowels.includes(word[i])) {
                        counter++; 
                    }
                }

                console.log("The word: " + word);
                console.log("Number of vowels: " + counter);
            
            } else {
                alert("Please enter a word!");
            }
        }