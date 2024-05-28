#include <iostream>

using namespace std;

int main(){
	char nama[25];
	
	struct data_tanggal{
		int tanggal;
		int bulan;
		int tahun;
	}
	
	tanggal_lahir;
	
	cout << "Nama anda : "; cin.getline(nama,sizeof(nama));
	cout << "Tanggal Lahir : "; cin >> tanggal_lahir.tanggal;
	cout << "Bulan Lahir : "; cin >> tanggal_lahir.bulan;
	cout << "Tahun Lahir : "; cin >> tanggal_lahir.tahun;
	cout << "Nama Lengkap : " << nama << endl;
	cout << "Tanggal Lahir : " << tanggal_lahir.tanggal << " - " << tanggal_lahir.bulan << " - " << tanggal_lahir.tahun << endl;
	
	return 0;
	
	
}
