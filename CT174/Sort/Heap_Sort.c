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
//thuat toan vun dong
void push_Down(recordtype a[], int first, int last) {
	int r = first;
	while(r <= (last-1)/2)
		if(last == 2*r+1) {
			if(a[r].key > a[last].key)
				swap(&a[r], &a[last]);
				r = last;
		} else
		if(a[r].key > a[2*r+1].key && a[2*r+1].key <= a[2*r+2].key) {
			swap(&a[r], &a[2*r+1]);
			r = 2*r+1;
		}else
		if(a[r].key > a[2*r+2].key && a[2*r+2].key < a[2*r+1].key) {
			swap(&a[r], &a[2*r+2]);
			r = 2*r+2;
		}
		else
			r = last;
}
void heap_Sort(recordtype a[], int n) {
	int i;
	for(i=(n-2)/2; i>=0; i--)
		push_Down(a,i,n-1);
	for(i=n-1; i>=2; i--) {
		swap(&a[0], &a[i]);
		push_Down(a, 0, i-1);
	}
	swap(&a[0], &a[1]);
}
int main() {
    recordtype a[100];
    int n;
    printf("Thuat toan Heap Sort: \n");
        read_Data(a, &n);
    printf("Du lieu truoc khi sap xep: \n");
        print_Data(a, n);
    printf("Du lieu sau khi sap xep: \n");
    heap_Sort(a, n);
        print_Data(a, n);
    return 0;
}