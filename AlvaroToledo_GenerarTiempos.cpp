#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
// Declaramos las funciones
int fibonacci (int N);
double get_time(int N);

//Main del codigo
int main(){
	int N = 35;
	for (int i=0; i<=N; i++){
		cout << i << " "<< get_time(i) << endl;
	}
	return 0;
}


//Sucesion de Fibonacci
int fibonacci (int N) {
	if (N==0){
		return 0;	
	}
	if (N==1){
		return 1;
	}
	else {
		return fibonacci(N-1)+fibonacci(N-2);	
	}
}

//Tiempo que se tarda en hacer la sucesion de Fibonacci

double get_time(int N){
	clock_t t;
	t = clock();
	// Corremos fibonacci(N)
	fibonacci(N); 
	t = clock() - t;
	float time = ((float)t)/CLOCKS_PER_SEC;
	return time;
}


