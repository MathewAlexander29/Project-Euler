#include <stdio.h>

// Function to calculate sum of AP for a given multiple and limit
long sum_of_ap(int multiple, int limit) {
    int n = (limit - 1) / multiple;     // number of terms below limit
    long first = multiple;
    long last = n * multiple;           // last term in the AP
    return n * (first + last) / 2;      // AP sum: n/2 * (a + l)
}

int main() {
    int limit = 1000;

    long sum3  = sum_of_ap(3, limit);   // Sum of multiples of 3
    long sum5  = sum_of_ap(5, limit);   // Sum of multiples of 5
    long sum15 = sum_of_ap(15, limit);  // Sum of multiples of 15 (common multiples)

    long total = sum3 + sum5 - sum15;

    printf("Sum of all multiples of 3 or 5 below %d is: %ld\n", limit, total);

    return 0;
}
