#include <stdio.h>
#include <stdlib.h>

int taille(const char* test){
    int i = 0;
    while (test[i] != '\0'){
        i++;
    }
    return i;
}
double calcul(const char* calcul, int pos, int pos_res, double res[]){
    double val = 0;
    switch (calcul[pos]) {
        case '+':
            val = res[pos_res - 2] + res[pos_res - 1];
            break;
        case '-':
            val = res[pos_res - 2] - res[pos_res - 1];
            break;
        case '*':
            val = res[pos_res - 2] * res[pos_res - 1];
            break;
        case '/':
            val = res[pos_res - 2] / res[pos_res - 2];
            break;
        }
    return val;
}

double parcour(int taille, const char* test){
    double val = 0;
    int j = 0;
    double result[20];
    for (int i = 0; i < taille; i++){
        if (test[i] < '1' || test[i] > '9'){
            val = calcul(test, i, j, result);
            result[j-2] = val;
            j = - 1;
        }else{
            val = test[i] - '0';
            printf("\nval = %lf",val);
            result[j] = val;
            j++;
        }
    }
    return result[0];
}

int main(){
    char* test = (char*) malloc(30 * sizeof(char));
    scanf("%s", test);
    printf("taille = %d \n", taille(test));

    printf("\nresultat = %lf",parcour(taille(test), test));

}