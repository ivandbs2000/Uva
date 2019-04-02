#include <iostream>
#include <vector>
#include <string>
using namespace std;

int contar( vector<string> vec,string c,int x){
	int xx,b = 0;
	for(xx =0 ; xx < x; xx++){
		if(c == vec[xx]){
			b = b + 1;
		}
	}
	return b;
}

int main(){
	int x,y,l,k,g,h = 0;
	int i,s,d,a;
	int t=0;
	string c;
	vector<string> arr(100);
	cin >> x >> y;
	while(x != 0){
		for(i = 0;i <x;i++){
			cin >> arr[i];
		}
		for(d = 0; d < y; d++){
			cin >> k >> g;
			for(a = 0; a < k;a++){
				cin >> c;
				t += contar(arr,c,x);
			}
			if(t >= g){
				h+= 1;
				t = 0;
				
			}
		}
		if(h == y){
			cout << "yes"<<endl;
		}
		else{
			cout << "no"<<endl;
		}
		t = 0;
		h = 0;
		cin >> x >> y;
	}
	
	return 0;
}