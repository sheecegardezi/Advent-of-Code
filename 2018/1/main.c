#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int convert_char_to_int( char character );
int main(int argc, char *argv[]) {


	FILE *fp;
	char buff[255];
	
	fp = fopen("input.txt", "r");
	
	int sum =0;
	
	//read each line from the file	
	while(fgets(buff, 255, (FILE*)fp)){
		
		
		// convert string to integer 		
		int lengthOfLine = strlen(buff) -1;
		int i = 0;
		bool currentIntegerPositiveSign=true;
		
		int currentInteger =0;
		//iterate over the string
		while(i<lengthOfLine){
			
			//first char is always sign
			if(i==0){
				if(buff[i]=='+'){
					currentIntegerPositiveSign=true;
				}else{
					currentIntegerPositiveSign=false;
				}
					
			}else{
				currentInteger = currentInteger *10;
				
				int charToint = convert_char_to_int(buff[i]);
			    
				currentInteger = (currentInteger +charToint);
				
			}
		
			i=i+1;	
		}
		
		if(currentIntegerPositiveSign){
			sum = sum + currentInteger;
		}else{
			sum = sum - currentInteger;
		}			
	}
	printf("sum: %i ", sum);
	
	
	fclose(fp);

	return 0;
}

int convert_char_to_int( char character ) {
	
   switch(character) {

   		case '0':
      		return 0;
   		case '1':
      		return 1;
   		case '2':
      		return 2;
   		case '3':
      		return 3;
   		case '4':
      		return 4;
   		case '5':
      		return 5;
   		case '6':
      		return 6;
   		case '7':
      		return 7;
   		case '8':
      		return 8;
   		case '9':
      		return 9;
  	   
	   default : 
		   return 0;
	}
}
