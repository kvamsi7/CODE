#include<stdio.h>
int main()
{
   int i,j,l,lc,num; 
  l = 1;
	scanf("%d",&num);
 	for(i = 1;i< num;i++){
  		
   	 if(i%2){               // checking whether even or not
    	for(j=1;j<=i;j++){
           if(j>1)
             printf("*");
        
	    	printf("%d",l);
            l=l+1;
        }
    printf("\n");
	}
    else{
         lc = l+i;
    	 for(j =1 ;j<=i;j++){
      		   if(j>1)
           		  printf("*");
       			
			lc--;
			printf("%d",lc);
    		l++;
        }
        printf("\n");
   }
}

return 0;
}
