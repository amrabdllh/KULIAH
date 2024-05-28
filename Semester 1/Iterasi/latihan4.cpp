#include <iostream>
#include <cstdlib>
using namespace std;
void hanoi (int n, char a, char b, char c) { if (n == 1)
cout <<" Pindahkan Cakram dari " <<a<< " ke " <<c<< "\n";
else {
hanoi (n-1, a, c, b);
hanoi (1, a, b, c);
hanoi (n-1, b, a, c); } }
int main (int argc, char *argv[]) {
int jml_cakram;
cout <<"================================\n";
cout <<"Simulasi Menara Hanoi\n";
cout <<"================================\n";
cout << "Masukkan Jumlah Cakram: ";
cin >> jml_cakram;
hanoi (jml_cakram, 'A', 'B', 'C');
cout << endl;
system ("PAUSE");
return EXIT_SUCCESS;
}
