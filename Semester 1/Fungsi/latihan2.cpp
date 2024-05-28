#include <iostream>
#include <cstdlib>

using namespace std;

int tambah(int x);
int main (){
	int a, hasil;
	cout << "Masukkan Bilangan : " ; cin >> a;
	cout << "a awal = " << a << endl;
	hasil = tambah(a);
	cout << "a akhir = " << a << endl;
	cout << "Hasil : " << hasil << "\n";
	system("PAUSE");
}

int tambah(int x){
	cout << "x awal = " << x << endl;
	x += 2;
	cout << "x akhir = " << x << endl;
	return x;
}
