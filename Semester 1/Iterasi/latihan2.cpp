#include <iostream>
#include <cstdlib>
using namespace std;
int faktorial (int x) {
if (x == 0 || x== 1)
return (1);
else
return (x*faktorial (x-1)); }
int main (int argc, char *argv[]) {
int y;
cout <<" Mencari Nilai Faktorial \n" << " Masukkan nilai y: ";
cin >> y;
cout <<" Faktorial Dari " << y << " adalah " << faktorial(y);
cout << endl;
system ("PAUSE");
return EXIT_SUCCESS;
 }
