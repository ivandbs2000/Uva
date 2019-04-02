#include <stack>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue> 
#include <math.h>

using namespace std;


vector<int> men(vector<int> n,vector<double> d,vector<int> pos){
	vector<int> ans;
	int pos1 = -1;
	double m1= 999999999999999999999.0;

	for(int i = 0; i < n.size();i++){
		if(d[i]!= -1){
			if(d[i] < m1){
				m1 = d[i];
				pos1 = i;
	 		}
			else{
				if(d[i] == m1){
					if( pos[(i*2)+1] < pos[(pos1*2) + 1] ){
						pos1 = i;
					}
					else{
						if(pos[(i*2)+1] == pos[(pos1*2) + 1]){
							if(pos[i*2] < pos[pos1*2]){
								pos1 = i;
							}
						}
					}
				}
			} 
		}
	}
	ans.push_back(pos1);
	pos1= -1;
	m1= 999999999999999999999.0;
	for(int i = 0; i < n.size();i++){
		if(d[i]!= -1 and ans[0] != i){
			if(d[i] < m1){
				m1 = d[i];
				pos1 = i;
	 		}
			else{
				if(d[i] == m1){
					if( pos[(i*2)+1] < pos[(pos1*2) + 1] ){
						pos1 = i;
					}
					else{
						if(pos[(i*2)+1] == pos[(pos1*2) + 1]){
							if(pos[i*2] < pos[pos1*2]){
								pos1 = i;
							}
						}
					}
				}
			} 
		}
	}

	ans.push_back(pos1);
	return ans;



}

vector<vector<int > > parse_tree(vector<int> v , int n){
	int i;
	vector<vector<int> > nod;
	
	for(i = 0; i < n;i++){
		vector<int> temp;
		for(int j = 0; j < n;j++){
			temp.push_back(-1);
		}
		nod.push_back(temp);
	}
	
	vector<vector<double> > dis;
	
	for(i = 0; i < n;i++){
		vector<double> p;
		for(int j = 0 ; j < n ; j++){
			p.push_back(-1.0);

		}
		dis.push_back(p);
		
	}

	

	int j=0;
	double d;
	i= 0;
	while(i < n*2){
		
		j= i+2;
		while(j < n*2){
			d = sqrt (pow( (v[j]-v[i]) , 2) + pow( (v[j+1]-v[i+1]) , 2) );
			
			nod[i/2][j/2] = j/2;
			nod[j/2][i/2] = i/2;
			dis[i/2][j/2] = d;
			dis[j/2][i/2] = d;
			j= j +2;
		}

		
		nod[i/2] = men(nod[i/2],dis[i/2],v); 
		i = i + 2;
	}
	
	return nod;
}

bool dfs(vector<vector<int > > v){
	
	stack<int> s;
	vector<int> visited;
	for(int i = 0; i < v.size();i++){
		visited.push_back(0);
	}
	s.push(0);
	visited[0] = 1;
	int j = 1,x;

	while(s.size() != 0){
		x  = s.top();
		s.pop();
		for(int k = 0; k < v[x].size() ; k++){
			if(visited[v[x][k]] != 1){
				s.push(v[x][k]);
				visited[v[x][k]] = 1;
				j+=1;
			}
		}
	}
	
	if(j  == v.size()){
		return true;
	}
	else{
		return false;
	}

}



int main(){
	int c,x;
	cin >>c;
	while (c!= 0){
		vector<int> vec;

		for(int j = 0; j < 2*c; j++){
			cin>>x;
			vec.push_back(x);
		}
		if(c > 2){
			vector<vector<int > > xd = parse_tree(vec,c);
			bool var = dfs(xd);
			if(var){
				cout<<"All stations are reachable." <<endl;
			}
			else{
				cout<<"There are stations that are unreachable."<<endl;
			}
		cin>>c;
		}
		else{
			cout<<"All stations are reachable." <<endl;
		}
	}
	return 0;
}