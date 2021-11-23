#include <stdio.h>

typedef int keytype;
typedef float othertype;

typedef struct {
    keytype key;
    othertype otherfields;
}recordtype;

void swap(recordtype *x, recordtype *y) {
    recordtype temp;
    temp = *x;
    *x = *y;
    *y = temp;
}
//doc file
void read_Data(recordtype a[], int *n) {
    FILE* f = freopen("data.txt","r",stdin);
    int i=0;
    if(f != NULL)
        while(!feof(f)) {
            fscanf(f,"%d%f", &a[i].key, &a[i].otherfields);
            i++;
        }
    else printf("Loi mo file\n");
    *n = i;
    fclose(f);
}
//in du lieu
void print_Data(recordtype a[], int n) {
    int i;
    for(i = 0; i<n; i++)
        printf("%3d %5d %8.2f\n", i+1, a[i].key, a[i].otherfields);
}
//thuat toan sap xep chon
void Selection_Sort(recordtype a[], int n) {
    int i, j, low_idx;
    keytype lowkey;
    for(i = 0; i<=n-2; i++) {
        lowkey = a[i].key;
        low_idx = i;
        for(j = i+1; j<=n-1; j++) {
            if(a[j].key < lowkey) {
                lowkey = a[j].key;
                low_idx = j;
            }
        }
        swap(&a[i], &a[low_idx]);
    }
}
int main() {
    recordtype a[100];
    int n;
    printf("Thuat toan Selection Sort: \n");
        read_Data(a, &n);
    printf("Du lieu truoc khi sap xep: \n");
        print_Data(a, n);
    printf("Du lieu sau khi sap xep: \n");
    Selection_Sort(a, n);
        print_Data(a, n);
    return 0;
}