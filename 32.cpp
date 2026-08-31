/*
 * We shall say that an n-digit number is pandigital
 * if it makes use of all the digits 1 to 9 exactly once;
 * for example, the 5-digit number, 1523, is 1 through 5 pandigital.
 *
 * The product 7254 is unusual, as the identity, 39 x 186 = 7254,
 * containing multiplicand, multiplier, and product is 1 through 9 pandigital.
 * Find the sum of all products whose multiplicand/multiplier/product identity can be written as a
 * 1 through 9 pandigital.
 * HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
 */


/* Let's have k digits to the left of the equation.
 * a digits on one side and k-a digits on the other.
 * The minimum value for a a-digit number is 10^(a-1)
 * The minimum value of the product is:
 * 10^(k-a-1) * 10^(a-1) = 10^(k-2) 
 * 10^(k-2) is a k-1 digit number. The sum of the 2 digits must be 9
 *
 *	k + (k-1) = 9: k = 5
 *	Thus k <= 5. And by virtue of the arrangement a * b = c
 *	k >= 2. We have bounds: Which is sufficient
 *	2 <= k <= 5
 *	
 *	For k = 2: a = 1; Largest number: 9 * 9 = 18: 2-digits
 *	RHS should have 9 - 2 = 7 digits, not 2
 *	Thus k != 2
 *
 *	For k = 3: a = 1; Largest number: 99 * 9 = 891: 3-digits
 *	RHS should have 9 - 3 = 6 digits, thus k != 3
 *	
 *	For k = 4: 
 *	a = 1; 
 *		Largest number: 999 * 9 = 8991: 4-digits
 *		RHS should have 9 - 4 = 5 digits > 4-digits, thus a != 1
 *	a = 2; 
 *		Largest number: 99 * 99 = 9801: 4-digits
 *		RHS should have 9 - 3 = 5 digits > 4-digits, thus k != 4
 *		Largest
 *
 *	For k = 5:
 *	a = 1:
 *		Largest number: 9999 * 9 = 89991: 5-digits
 *		RHS should have 9-5 = 4 digits < 5-digits, thus a = 1 is within range
 *	a = 2:
 *		Largest number: 999 * 99 = 98901: 5-digits
 *		RHS should have 9-5 = 4 digits < 5-digits, thus a = 2 is within range
 *	Thus k = 5
 */

#include <set>
#include <vector>
#include <string>
#include <iostream>
void permutate(std::vector<std::string> set, std::vector<std::string>& items, int choose = -1, std::string built = ""){
	for(int a = 0;a < set.size();a++){
		std::string made = built + set[a];
		std::vector<std::string> remaining = set;
		remaining.erase(remaining.begin() + a);

		if (made.length() == choose|| remaining.size() == 0){
			items.push_back(made);
			continue;
		}
		permutate(remaining, items, choose, made);
	}
}

int main(int argc, char** argv){
	std::vector<std::string> characters;
	for(int i = 1;i<=9;i++)
		characters.push_back(std::to_string(i));

	// Load all the arrangements
	std::vector<std::string> arrangements;
	permutate(characters, arrangements);

	int total = 0;
	std::set<int> seen; 
	// Check the combinations
	for (int i = 0; i < arrangements.size();i++){
		int result = std::stoi(arrangements[i].substr(5));
		if (seen.find(result) != seen.end()){
			continue;
		}
		for (int a = 1; a <= 2;a++){
			int num1 = std::stoi(arrangements[i].substr(0,a));
			int num2 = std::stoi(arrangements[i].substr(a,5-a));
			if (num1 * num2 == result){
				seen.insert(result);
				total += result;
			}
		}
	}
	std::cout << total << std::endl;
	return 0;
}
