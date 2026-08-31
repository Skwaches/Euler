/*
 * The number, 197, is called a circular prime
 * because all rotations of the digits: 197, 971, and 719, are themselves prime.
 * There are thirteen such primes below 100:
 * 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97
 * How many circular primes are there below one million?
 */

#include <algorithm>
#include <set>
#include <vector>
#include <iostream>

// Elements kinda cycle.
// First become last, 2 becomes 1 and so forth.
void rotations(std::string number, std::vector<std::string>& items){
	items.push_back(number);
	std::string temp = number;
	int rotated = 0;
	while(rotated < number.length() - 1){
		char saved = temp[0];
		temp = temp.substr(1);
		temp += saved;
		auto iterator = std::find(items.begin(),items.end(),temp);
		if (iterator == items.end())
			items.push_back(temp);
		rotated++;
	}
}	
/*
 * This is copied straight from question 32.
 * Slightly modified to allow selection with replacement
 * Wish there were a nice import mechanism like in python*/
void permutate(std::vector<std::string> set, std::vector<std::string>& items, int choose = -1 , bool replacement = false, std::string built = ""){
	for(int a = 0;a < set.size();a++){
		std::string made = built + set[a];
		std::vector<std::string> remaining = set;
		if (!replacement)
			remaining.erase(remaining.begin() + a);

		if (made.length() == choose|| remaining.size() == 0){
			auto found = std::find(items.begin(),items.end(),made);
			if (found == items.end())
				items.push_back(made);
			continue;
		}
		permutate(remaining, items, choose, replacement, made);
	}
}

std::vector<int> primes;
bool isPrime(int n){
	if (n <= 1)
		return false;
	auto found = std::find(primes.begin(),primes.end(),n);
	if (found != primes.end()){
		return true;
	}
	int lowerBound = (int)(n/2 + 1);
	for (int i = 2; i <= lowerBound; i++)
		if (n%i == 0){
			return false;
		}

	primes.push_back(n);
	return true;
}

// Number is made up of 1,3,7 and 9
// Range of < 10^6 means maximum of 6 digits.
std::vector<std::string> availablePossibilities(){
	std::vector<std::string> items = {"1","3","7","9"};
	std::vector<std::string> numbers;
	for(int k = 1; k <= 6; k++){
		permutate(items,numbers,k,true);
	}
	return numbers;
}
void solution(){
	std::vector<std::string> found = {"2","5"};
	std::set<std::string> reviewed;
	std::vector<std::string> availableOptions = availablePossibilities();

	for(std::string number:availableOptions){
		auto iterator = std::find(reviewed.begin(),reviewed.end(),number);
		if (iterator != reviewed.end())
			continue;
		std::vector<std::string> circles;
		rotations(number,circles);
		bool problem = false;
		for (auto circle: circles){
			reviewed.insert(circle);
			if (!problem){
				int value = std::atoi(circle.data());
				problem = !isPrime(value);
			}
		}
		if (!problem)
			found.insert(found.end(),circles.begin(),circles.end());
	}
	std::cout<< std::endl << found.size() << std::endl;
}

int main(int argc, char** argv){
	solution();
}

