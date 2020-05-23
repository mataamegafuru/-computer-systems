#include <iostream> 
#include <math.h> 
using namespace std; 
double f(double x){return (-3*x*x+2*x+9);} 
double I(double a,double b,int n,double y){return ((b-a)/(2*n)*y);} 
int main() { double n; double a,b,y,dy,In; //cin>>a>>b>>n;
a = 1; b = 1000000; n = 2000000000;
if (n>1){ dy=(b-a)/n; y+=f(a)+f(b); for (int i=1; i<n; i++) {y+=2*(f(a+dy*i));} In=I(a,b,n,y); cout << In; } else {cout << "Wrong data";} }
