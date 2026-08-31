/*
 * 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
 * Find the sum of all numbers which are equal to the sum of the factorial of their digits.
 * NOTE: As 1! = 1 and 2! = 2 are not sums they are not included.
*/

/*
 * For a K-digit number:
 * Largest factorial sum = 9! x K = F	
 * Smallest number = 10^(K-1) = N:
 * for the equation to be solvable; F >= N
 * This is the case for K <= 7.
 * Since a sum is required K >= 2.
 */

#include <iostream>
#include <string>
static int cache[10];
void initFactorial(){
	cache[0] = 1;
	for (int i = 1;i < 10;i++){
		cache[i] = cache[i-1] * i;
	}
}

int factorialSum(int number){
	std::string digits = std::to_string(number);
	int total = 0;
	for(auto digit: digits){
		int value = digit - '0';
		 total += cache[value];
	}
	return total;
}

void solution(){
	initFactorial();
	int total = 0;
	for(int k = 10; k < 10000000; k++){
		if (factorialSum(k) == k){
			total += k;
		}
	}
	std::cout << total << std::endl;
}
int main(int argc, char** argv){
	solution();
}
