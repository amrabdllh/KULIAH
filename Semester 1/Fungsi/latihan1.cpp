#include <iostream>

using namespace std;

int data = 100;
void fungsi_satu();
void fungsi_dua();

int main(){
	int data = 200;
	fungsi_satu();
	fungsi_dua();
	
	cout << "Nilai data lokal main = " << data << endl;
	system("PAUSE");
}

void fungsi_satu(){
	int data = 300;
	cout << "Nilai data lokal satu = " << data << endl;
}


void fungsi_dua(){
	cout << "Nilai data eksternal = " << data << endl;
}
