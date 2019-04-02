#include <iostream>
#include <vector>
using namespace std;

vector<int> zero(vector<int> vec){
	int l ;
	for( l = 0; l < 26 ; l++){
		vec[l] = 0;
	}
	return vec;
}


int main(){
	int n,k;
	int i = 1,c= 1,l = 1,s = 0;
	vector<int> vec(26);
	cin >> n >> k;
	while(n != 0){
		//cout << " ";
		while(c <= n){
			if(l > k){
				l = 1;
			}
			if(vec[i] != -1){
				if(s == 0){
					vec[i] += l ;
					l += 1 ;
				}
				if(s > 0){
					vec[i] += s ;
					s = 0;
				}
				
				if(vec[i] >= 40){
					//l += 1;
					s += vec[i] - 40;
					c += 1;
					vec[i] = -1;
					if(i < 10){
						cout << "  " << i ;
					}
					if(i >= 10){
						cout << " " << i ;
					}
				}
				
				
			}
			i ++;
			if(i > n){
				i = 1;
			}
		}
		
		l = 1;
		cout <<endl;
		vec=zero(vec);
		cin >> n >> k;
		c = 1;
		i = 1;
		s = 0;
	}
	return 0;
}


