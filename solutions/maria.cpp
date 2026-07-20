#include <iostream>
using namespace std;

int main() {

    int numbers[] = {15, 42, 7, 89, 23, 3};
    int size = sizeof(numbers) / sizeof(numbers[0]);

  
    int maxVal = numbers[0];
    int minVal = numbers[0];


    for (int i = 1; i < size; i++) {
        if (numbers[i] > maxVal) {
            maxVal = numbers[i];
        }
        if (numbers[i] < minVal) {
            minVal = numbers[i];
        }
    }

   
    cout << "Maximum value: " << maxVal << endl;
    cout << "Minimum value: " << minVal << endl;

    return 0;
}