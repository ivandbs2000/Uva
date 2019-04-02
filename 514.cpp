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



int main(){
	int x,y;
	cin>>x;
	while(x != 0){
		cin>>y;
		while(y != 0){
			bool band = true;
			int c = 0;
			stack<int> pil;
			//pil.push(1);

			for(int i = 0;i< x-1;i++) {
				if(c < y){
					for(int j = c+1 ;j <= y; j++){
							pil.push(j);
							
					}			
					c = y;
				}
				if(y != pil.top()){
					band = false;
				}
				else{
					
					pil.pop();
				}
				cin>>y;
			}
			if(band){
				cout<<"Yes"<<endl;
			}
			else{
				cout<<"No"<<endl;
			}
			cin>>y;
			
		}
		cout<<endl;
		cin>>x;
	}
	return 0;
}