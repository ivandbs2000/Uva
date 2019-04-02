#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class DNA{
public:
	string ca;
	int des;
	DNA(){
		ca = ' ';
		des = 0; 
	}
};

int calcular(string cadena){
	int l = 1;
	for(int j = 0; j < cadena.size();j++){
		for(int i = j  ; i < cadena.size();i++){
			if(cadena[j] > cadena[i]){
				l++;
			}
		}
	}
	return l;
}

bool comparar(DNA m,DNA n){
	
	return m.des < n.des;
}

int main(){
	int x,y,z;
	string l;
	vector<DNA> vec;
	cin>>x;
	for(int i = 0;i<x;i++){
		if(i >0){
			cout <<endl;
		}
		cin>> y >> z;
		for(int j = 0;j < z; j++){
			cin >> l;
			DNA t;
			t.ca = l;
			t.des = calcular(l);
			vec.push_back(t);
		}
		stable_sort(vec.begin(),vec.end(),comparar);
		for(int f = 0; f < vec.size();f++){
			cout << vec[f].ca << endl;
		}
		vec.clear();
	}
	return 0;
}