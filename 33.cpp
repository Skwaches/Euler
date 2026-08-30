/*
 * The fraction 49/48 is a curious fraction,
 * as an inexperienced mathematician
 * in attempting to simplify it may incorrectly believe that: 49/98 = 4/8
 * ,which is correct, is obtained by cancelling the 9s.
 * We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
 * There are exactly four non-trivial examples of this type of fraction,
 * less than one in value, and containing two digits in the numerator and denominator.
 * If the product of these four fractions is given in its lowest common terms,
 * find the value of the denominator.
 * */

// Fraction is of the form:
// 		ab/ac		ab/ca
// 		ba/ac 		ba/ca
// a is the digit in the tens or ones position that matches,
// b and c are the others that don't match
// b != c
// numerator < denominator

#include <iomanip>
#include <iostream>
#include <vector>
typedef struct Fraction{
	int numerator,denominator;
}Fraction;

void solution(std::vector<Fraction>& viable){
	Fraction found;
	std::cout << std::setprecision(4);
	std::cout << std::fixed;
	for(int a = 1;a<=9;a++){
		for(int b = 1;b<=9;b++){
			std::vector<int> numerators;
			numerators.push_back(10 * a + b);
			if (a != b)
				numerators.push_back(10 * b + a);

			for(int c = b + 1;c <= 9;c++){
				std::vector<int> denominators;
				denominators.push_back(10 * a + c);
				if (a != c)
					denominators.push_back(10 * c + a);

				for (int numerator: numerators){
					for (int denominator: denominators){
						found = {numerator,denominator};
						float fractal = (float)(numerator)/(float)(denominator);
						if (fractal >= 1.f)
							continue;
						float stripped = (float)(b)/(float)(c);
						if (fractal == stripped)
							viable.push_back(found);
					}
				}
			}
		}
	}
}

void simplify(Fraction& fraction){
	int divisor = 2;
	while(true){
		if (divisor > fraction.numerator || divisor > fraction.denominator)
			break;
		while(fraction.numerator%divisor == 0 && fraction.denominator%divisor == 0){
			fraction.numerator /= divisor;
			fraction.denominator /= divisor;
		}
		divisor++;
	}
}
int main(int argc, char** argv){
	std::vector<Fraction> viable;
	solution(viable);
	Fraction product = {1,1};
	for (auto fraction: viable){
		product.numerator *= fraction.numerator;
		product.denominator *= fraction.denominator;
	}
	simplify(product);
	std::cout << product.denominator << std::endl;
	return 0;
}
