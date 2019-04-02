
#include <stdio.h>
int fun(int x){
	int temp;
	temp = ((((((x*567)/9) + 7492) *235)/47)-498);
	return temp;
}

int main(){
	int t,n,c = 0,total,tem;
	scanf("%d",&t);
	while( c < t){
		scanf("%d",&n);
		total = fun(n);
		total = total/10;	
		total = total%10;
		if(total < 0){
			total = total*-1;
		}
		printf("%d\n",total);
		c++;
	}
	return 0;
}
