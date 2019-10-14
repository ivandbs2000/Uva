#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std;

int pow[4] = {1,2,4,8};
int tree[4000000][4];
int lazy[4000000] = {0};

class SegTree{
private:
	int N,c,aco;
	bool band;
public:
	SegTree(int* temp,int low,int hi){
		N = hi;
		build(temp,0,low,hi);
	}

	void build(int* ans , int node,int low,int hi){
		if(low == hi){
			if(ans[low] == 1){
				tree[node][0]= low;
				tree[node][1] = -1;
				tree[node][2]= low;
				tree[node][3] = 5000000;
			}
			else{
				tree[node][0]= -1;
				tree[node][1] = low;
				tree[node][2]= 5000000;
				tree[node][3] = low;
			}
		}
		else{

			int left=1+ (node<<1), right = 2 + (node<<1);
			int mid = low+ ((hi-low)>>1);
			build(ans,left,low,mid);
			build(ans,right,mid+1,hi);
			tree[node][0] = maxx(tree[left][0],tree[right][0]);
			tree[node][1] = maxx(tree[left][1],tree[right][1]);
			tree[node][2] = mim(tree[left][2],tree[right][2]);
			tree[node][3] = mim(tree[left][3],tree[right][3]);
		}
	}

	int maxx(int x,int y){
		if(x>y){return x;}
		else{return y;}
	}

	int mim(int x,int y){
		if(x<y){return x;}
		else{return y;}
	}

	void neg(int node){
		int temp = tree[node][0];
		tree[node][0] = tree[node][1];
		tree[node][1] = temp;
		temp = tree[node][2];
		tree[node][2] = tree[node][3];
		tree[node][3] = temp;
	}

	void update(int node, int low , int hi, int l,int r){//low hi 0 ,n y l r x,y
		int left=1 +(node<<1), right = 2 + (node<<1);
		if(lazy[node]!= 0){
			if(lazy[node]%2 != 0){
				neg(node);
			}
			if(low!=hi){
				lazy[left] += lazy[node];
				lazy[right] += lazy[node];
			}
			
			lazy[node] = 0;
		}

		if(l > hi or r < low){
			return;
		}

		if(l <= low and r>=hi){//encuentro el que esta contenido y actualizo sus hijos
			neg(node);
			if(low!=hi){
				lazy[left] += 1;
				lazy[right] += 1;
			}
			return;
		}

		int mid = low+ ((hi-low)>>1);
		update(left,low,mid,l,r);
		update(right,mid+1,hi,l,r);
		tree[node][0] = maxx(tree[left][0],tree[right][0]);
		tree[node][1] = maxx(tree[left][1],tree[right][1]);
		tree[node][2] = mim(tree[left][2],tree[right][2]);
		tree[node][3] = mim(tree[left][3],tree[right][3]);
	}
	//check
	int queryMa(int node, int low , int hi, int l,int r){
		int left=1 +(node<<1), right = 2 + (node<<1);
		if(lazy[node]!= 0){
			
			if(lazy[node]%2 != 0){
				neg(node);
			}

			if(low!=hi){
				lazy[left] += lazy[node];
				lazy[right] += lazy[node];
			}
			
			lazy[node] = 0;
		}
		if(l>hi || r<low){
			return -1;
		}

		if(l <= low and r>=hi){
			return tree[node][0];
		}

		int mid = low+ ((hi-low)>>1);
		return maxx(queryMa(left, low , mid, l, r),queryMa(right, mid+1 ,hi, l,r));
	}
	//check
	int queryMi(int node, int low , int hi, int l,int r){
		int left=1 +(node<<1), right = 2 + (node<<1);
		if(lazy[node]!= 0){
			
			if(lazy[node]%2 != 0){
				neg(node);
			}
			
			if(low!=hi){
				lazy[left] += lazy[node];
				lazy[right] += lazy[node];
			}
			
			lazy[node] = 0;
		}
		if(l>hi || r<low){
			return 5000000;
		}

		if(l <= low and r>=hi){
			return tree[node][2];
		}

		int mid = low+ ((hi-low)>>1);
		return mim(queryMi(left, low , mid, l, r),queryMi(right, mid+1 ,hi, l,r));
	}
	//check
	void query_real(int x,int y){
		int low,hi;
		if(x == 0){low = 0;}
		else{
			if(queryMa(0,0,N,x,x) == -1){
				low = queryMa(0,0,N,0,x-1);
				if(low == -1){
					low = x;
				}
			}
			else{
				low = x;
			}
		}

		if(y == N){hi = N;}
		else{
			if(queryMa(0,0,N,y,y) == -1){
				hi = queryMi(0,0,N,y+1,N);
				if(hi == 5000000){
					hi = y;
				}
			}
			else{
				hi = y;
			}
		}
		update(0,0,N,low,hi);
	}

	char desc(int g){
		char r;
		if(g == 10){
			r = 'A';
		}
		else if(g == 11){
			r = 'B';
		}
		else if(g == 12){
			r = 'C';
		}
		else if(g == 13){
			r = 'D';
		}
		else if(g == 14){
			r = 'E';
		}
		else if(g == 15){
			r = 'F';
		}
		else{
			r = '0' + g;
		}
		return r;
	}
	//check
	void final(int node, int low, int hi){
		int left=1 +(node<<1), right = 2 + (node<<1);
		if(lazy[node]!= 0){
			
			if(lazy[node]%2 != 0){
				neg(node);
			}
			

			if(low!=hi){
				lazy[left] += lazy[node];
				lazy[right] += lazy[node];
			}
			
			lazy[node] = 0;
		}
		if(low == hi){
			if(tree[node][0] != -1){
				aco+=pow[c];
			}
			c--;
			if(c < 0){
				char var =desc(aco);
				if(band == false and var=='0'){
					c = 3;
				}
				else{
					cout<<var;
					band = true;
				}
				c= 3;
				aco = 0;
			}
		}
		else{
			int mid = low+ ((hi-low)>>1);
			final(left,low,mid);
			final(right,mid+1,hi);
		}
	}

	void print(){
		c = N%4;
		aco = 0;
		band = false;
		final(0,0,N);
		if(band == false){
			cout<<'0';
		}
		cout<<endl;
	}
};

void pas(int* ans, char g,int x,int ind){
	int r ,j = x;
	if(g == 'A'){
		r = 10;
	}
	else if(g == 'B'){
		r = 11;
	}
	else if(g == 'C'){
		r = 12;
	}
	else if(g == 'D'){
		r = 13;
	}
	else if(g == 'E'){
		r = 14;
	}
	else if(g == 'F'){
		r = 15;
	}
	else{
		r = (int)g - 48;
	}
	for(int i = ind;i >= 0;i--){
		if(pow[i] <= r){
			ans[j] = 1;
			r-= pow[i];
		}
		else{
			ans[j] = 0;
		}
		j++;
	}
}

void convert(int* ans,string s,int n){
	int j = n-4,r = n-1;
	for(int i = s.size() -1;i >= 0; i--){
		if(j< 0){
			pas(ans,s[i],0,r);
		}
		else{
			pas(ans,s[i],j,3);
		}
		j-=4;
		r-=4;
	}
}

int main(){
	int q,x,y,n;
	string temp;
	int cases;
	cin>>cases;
	for(int g = 0; g < cases;g++){
		cin>>n>>q;
		cin>>temp;
		int* ans = new int[n];
		convert(ans,temp,n);
		SegTree s(ans,0,n-1);
		for(int b = 0;b < q;b++){
			cin>>x>>y;
			s.query_real(x-1,y-1);
		}
		s.print();
	}
	return 0;
}