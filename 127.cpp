#include <stack>
#include <iostream>
#include <string.h>
#include <iterator>
#include <algorithm>
#include <vector>
#include <queue> 
#include <map> 
#include <functional>

using namespace std;

struct Carta{
	char face;
	char suit;
};

bool comparacion( Carta c1,  Carta c2) {
    if(c1.suit==c2.suit || c1.face==c2.face){
    	return true;
    }
    return false;
}
int main(){
	string h;
	Carta temp;
	while(true){
		vector<stack<Carta> > vec(52);
		cin>>h;
		if(h == "#"){
			break;
		}
		temp.face = h[0];
		temp.suit = h[1];
		vec[0].push(temp);
			
		for(int j = 1; j < 52; j++){
			cin>>h;;
			temp.face = h[0];
			temp.suit = h[1];
			vec[j].push(temp);
			
		}
		
		int k = (vec.size());
		
		for(int i = 0; i < k; i++ ){
			if( i >= 3 && comparacion((vec[i]).top(), (vec[i-3]).top())){
					vec[i-3].push(vec[i].top());
					vec[i].pop();
					if(((vec[i]).empty())){
						vec.erase(vec.begin() + i);
						k--;
					}
							
					i = i-4;
					
				
			}	
			else if( i>= 1 && comparacion((vec[i]).top(), (vec[i-1]).top())){		
				 
					vec[i-1].push(vec[i].top());
					vec[i].pop();
					if(((vec[i]).empty())){
						vec.erase(vec.begin() + i);
						k--;
					}
					i = i-2;
				
			}
			
		}
		if(vec.size() == 1){
			cout<<vec.size()<<" "<<"pile remaining:";
		}
		else{
			cout<<vec.size()<<" "<<"piles remaining:";
		}
		for(int i = 0; i < vec.size();i++){
			cout<<" "<<vec[i].size();
			
		}
		cout<<endl;
		
	}
	return 0;
}
