#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string transformar(string s){
	string temp;
	int c = 0;
	int i = 0;
	for(int i = 0;i< s.size();i++){
		if(c == 3){
			temp.push_back('-');
			i--;
			c++;
		}
		else if(s[i] >= '0' && s[i] <= '9'){
			temp.push_back(s[i]);
			c++;
		}
		else if(s[i] == 'A' || s[i] == 'B' || s[i] == 'C'){
			temp.push_back('2');
			c++;
		}
		else if(s[i] == 'D' || s[i] == 'E' || s[i] == 'F'){
			temp.push_back('3');
			c++;
		}
		else if(s[i] == 'G' || s[i] == 'H' || s[i] == 'I'){
			temp.push_back('4');
			c++;
		}
		else if(s[i] == 'J' || s[i] == 'K' || s[i] == 'L'){
			temp.push_back('5');
			c++;
		}
		else if(s[i] == 'M' || s[i] == 'N' || s[i] == 'O'){
			temp.push_back('6');
			c++;
		}
		else if(s[i] == 'P' || s[i] == 'R' || s[i] == 'S'){
			temp.push_back('7');
			c++;
		}
		else if(s[i] == 'T' || s[i] == 'U' || s[i] == 'V'){
			temp.push_back('8');
			c++;
		}
		else if(s[i] == 'W' || s[i] == 'X' || s[i] == 'Y'){
			temp.push_back('9');
			c++;
		}
		
	}
	return temp;
}


int main(){
	int x,y,z = 1,l = 0;
	vector<string> vec(100000);
	string g;
	cin >> x;
	for(int i = 0; i < x;i++){
		if(i > 0){
			cout<<endl;
		}
		cin >> y;
		for(int j = 0; j < y;j++){
			cin >> g;
			vec[j] = transformar(g);
		}
	    vector<string>::iterator it = vec.begin() + y;
	    sort(vec.begin(),it);
	    for(int j = 0;j < y;j++){
	    	if(vec[j] == vec[j+1]){
	    		z++;
	    		l = 1;
	    	}
	    	else if(z > 1){
	    		cout << vec[j] << ' ' << z << endl;
	    		z = 1;
	    	}
	    }
	    if(l == 0){
	    	cout <<"No duplicates."<<endl;
	    }
	    z = 1;
	    l = 0;
	    vec.clear();
	}
	return 0;
}