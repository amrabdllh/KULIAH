#include <iostream>
#include <cstdlib>
using namespace std;
unsigned int pangkat (int x, int y) {
int hasil = 1, i;
for (i=1; i<= y; i++){
hasil = hasil*x; }
return hasil; }
int main(int argc, char** argv) {
int x,y;
x = 6;
y = 2;
cout << x << " Pangkat " << y << " = ";
cout << pangkat (x,y) <<endl;
system ("PAUSE");
return 0;
}
