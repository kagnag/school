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
//cai dat quicksort
//chon chot
int find_Pivot(recordtype a[], int i, int j) {
	keytype first_key;
	int k;
	k = i+1;
	first_key = a[i].key;
	while( k<=j && a[k].key == first_key)
		k++;
	if(k>j)
		return -1;
	else 
		if(a[k].key > first_key)
			return k;
		else 
			return i;
}
//phan hoach
int partition(recordtype a[], int i, int j, keytype pivot) {
	int L, R;
	L = i;
	R = j;
	while(L<=R) {
		while(a[L].key < pivot)
			L++;
		while(a[R].key >= pivot) 
			R--;
		if(L<R)
			swap(&a[L],&a[R]);	
	}
	return L;
}
//thuat toan sap xep nhanh
void quick_Sort(recordtype a[], int i, int j) {
	keytype pivot;
	int pivot_idx, k;
	pivot_idx = find_Pivot(a, i ,j);
	if(pivot_idx != -1) {
		pivot = a[pivot_idx].key;
		k = partition(a, i ,j, pivot);
		quick_Sort(a, i, k-1);
		quick_Sort(a, k, j);
	}
}

int main() {
    recordtype a[100];
    int n;
    printf("Thuat toan Quick Sort: \n");
        read_Data(a, &n);
    printf("Du lieu truoc khi sap xep: \n");
        print_Data(a, n);
    printf("Du lieu sau khi sap xep: \n");
    quick_Sort(a, 0, n-1);
        print_Data(a, n);
    return 0;
}