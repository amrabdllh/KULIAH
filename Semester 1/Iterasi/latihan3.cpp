#include <iostream>
#include <cstdlib>
using namespace std;
long fibo (long n) {
if ((n == 1 || n== 2))
return 1;
else
return fibo (n-1) + fibo (n-2); }
int main (int argc, char *argv[]) {
int x;
cout <<"========================================\n";
cout <<" Mencari Nilai Fibonaccy \n";
cout <<"========================================\n";
cout << "Masukkan nilai x : ";
cin >> x;
cout <<"Mencari Nilai Fibonaccy \n";
cout << "Nilai dari " << x << " adalah " << fibo(x);
cout << endl;
system ("PAUSE");
return EXIT_SUCCESS;
}
