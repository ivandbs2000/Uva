#include <stdio.h>
#include <stdlib.h>





int comparar(int*arr,int s,int j){
	int i;
	for(i = s; i < j+1; i += s){
		if(i%7 != 0 && (1+i)%7 != 0){
			arr[i] = 1;
		}
	}
}

int contar(int*arr,int s){
	int i,h=0;
	for(i = 1; i<s+1; i++ ){
		if(arr[i] == 1){
			h++;
		}
	}
	return h;
}
int zero(int*arr){
	int i;
	for(i=0 ; i < 3651 ; i++){
		arr[i] = 0;
	}
}

int main(){
	int d,e,j,w,f;
	int v,x;
	scanf("%d",&d);
	for(v=0;v<d;v++){
		int s[3651];
		scanf("%d", &e);
		scanf("%d", &j);
		for(x = 0; x<j ; x++){
			scanf("%d", &w);
			comparar(s,w,e);
		}
		f = contar(s,e);
		printf("%d\n",f);
		zero(s);
	}
	return 0;
}

