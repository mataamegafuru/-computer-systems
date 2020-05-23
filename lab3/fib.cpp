#include <iostream>
using namespace std; 
unsigned long long int f(int n) 
{ 
	if(n == 0) return 0; 
	if(n == 1 || n == 2) return 1; 
	return f(n-1)+f(n-2); 
} 
int main() 
{ 
	cout << f(45) << endl; 
	return 0; 
}
