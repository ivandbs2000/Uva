#include <iostream>
#include <vector>
#include <string>
#include "stdlib.h"
#include <algorithm>
using namespace std;

string verificar(string d,string q){
	int l= 1;
	string s;
	for(int y = 0; y < q.size();y++ ){
		if(d[y] == q[y]){
			l++;
		}
	}

	for(int x = l; x <d.size();x++){
		s.push_back(q[x]);
	}
	return s;
}

int main(){
	int x,l= 0,f=0,c= 1;
	vector<string> vec(100000) ;
	string a;
	cin >> x;
	while(x!= 0){
		
		for(int i = 0;i < x;i++){
			cin >> vec[i];
		}
		printf("Case %i:\n",c);
		for(int j = 0;j < x;j++){

			int yu = atoi(vec[j].c_str());
			int yy = atoi(vec[j+1].c_str());
			
			if(yu == yy-1){	
				l++;
			}
			else if(l == 0){
				cout << vec[j] << endl;
				f++;
			}
			else if(l > 0){
				//a = verificar(vec[f],vec[j]);
				int yi =  atoi(vec[f].c_str());
				int hu =  atoi(vec[j].c_str());
				int ss = yi-hu;
				cout << vec[f] <<'-';
				string z = vec[f];
				for(int w = 0;w<ss;w++){
					cout << "xd"<<z[w] ;
				}
			    f += l+1;
				l = 0;
				a = "";
			    cout <<endl;
			}
		}
		l = 0;
		f = 0;
		c++;
		cout<<endl;
		vec.clear();
		cin>>x;

	}
	return 0;
}