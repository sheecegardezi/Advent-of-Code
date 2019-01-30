#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int convert_char_to_int( char character );
int convert_string_to_int(char string[]);
bool check_number_in_array(int number, int*array);


int main(int argc, char *argv[]) {


	FILE *fp;
	char buff[255];
	
	fp = fopen("input.txt", "r");
	
	int countOfInputNumbers = 1004;
	int * listOfInputNumbers = (int *) malloc(countOfInputNumbers * sizeof(int));
	
	//read each line from the file	
	int numberOfLines = 0;
	for(numberOfLines=0;fgets(buff, 255, (FILE*)fp);numberOfLines=numberOfLines+1){
		
		int lengthOfLine = strlen(buff);

		if(lengthOfLine>1){
			int currentInputNumber = convert_string_to_int(buff);
			listOfInputNumbers[numberOfLines]=currentInputNumber;
			

		}
		
	}
	
	int *listOfSums= (int *) malloc(1004000 * sizeof(int));;
	int i = 0;
	int j=0;
	int sum=0;
	while(true){
		
		if(i==numberOfLines){
			i=0;
		}
		
		sum=sum +listOfInputNumbers[i];
		
		
		int k;
		for(k=0;k<j;k=k+1){
			if(listOfSums[k]==sum){
				printf("repeat %i \n",sum);
				return 0;
			}
		} 
		listOfSums[j]=sum;
		j=j+1;
			
		i=i+1;
	}
	
	
	
	fclose(fp);

	return 0;
}


bool check_number_in_array(int number, int array[]){
	int lengthOfArray = sizeof(array)/sizeof(array[0]);

	int i = 0;
	for(i = 0; i < lengthOfArray; i++){
		
		printf(" %inumber: %i \n", i, number);
		if(number == array[i]){
			return true;
		}
	}
	return false;
}

int convert_string_to_int(char string[]){
	
	// convert string to integer 		
	int lengthOfLine = strlen(string);
		
	
	int i = 0;
	bool positiveSignFlag=true;
	
	
	int currentInteger = 0;
	//iterate over the string
	for(i=0;i<lengthOfLine;i=i+1){
		
		//first char is always sign
		if( i == 0 && (string[i] == '+' || string[i] == '-')){
			if(string[i] == '+'){
				positiveSignFlag=true;
			}else{
				positiveSignFlag=false;
			}
				
		}else{
			
			int charToint = convert_char_to_int(string[i]);
			if(charToint>-1){
				currentInteger = currentInteger *10;
				currentInteger = (currentInteger +charToint);	
			}
			
		}
	
	}
	
	if(positiveSignFlag){
		return currentInteger;
	} 
	
	currentInteger = currentInteger *-1;
	return currentInteger;	
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
		   return -1;
	}
}
