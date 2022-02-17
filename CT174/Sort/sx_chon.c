#include <stdio.h>

typedef int keytype;
typedef float othertype;

const char* sort[] = {"Selection Sort","Bubble Sort","Insertion Sort","Quick Sort","Quick Sort Bien The","Heap Sort"};

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
FILE *f;
f = fopen("data.txt","r");
int i=0;
if(f != NULL)
	while(!feof(f)) {
		fscanf(f,"%d%f", &a[i].key,&a[i].otherfields);
		i++;
	}
else printf("Loi mo file\n");
fclose(f);
*n = i;
}
//in du lieu
void print_Data(recordtype a[], int n) {
int i;
for(i=0; i<n; i++) 
	printf("%3d %5d %8.2f\n", i+1, a[i].key, a[i].otherfields);
}
//thuat toan sap xep chon
void selection_Sort(recordtype a[], int n) {
int i, j, low_idx;
keytype lowkey;
for(i=0; i<=n-2; i++) {
	lowkey = a[i].key;
	low_idx = i;
	for(j = i+1; j<=n-1; j++) {
		if(a[j].key < lowkey){
			lowkey = a[j].key;
			low_idx = j;
		}
	}
	swap(&a[i], &a[low_idx]);
}
}
//thuat toan sap xep xen
void insertion_Sort(recordtype a[], int n) {
int i, j;
for(i=1; i<=n-1; i++) {
	j=i;
	while(j>0 && (a[j].key < a[j-1].key)) {
		swap(&a[j],&a[j-1]);
		j--;
	}
}
}
//thuat toan sap xep noi bot
void bubble_Sort(recordtype a[], int n) {
int i, j;
for(i=0; i<=n-2; i++)
	for(j=n-1; j>=i+1; j--) 
		if(a[j].key < a[j-1].key)
			swap(&a[j], &a[j-1]);
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
//cai dat quicksort bien the
//chon chot bien the
int find_Pivot2(recordtype a[], int i, int j) {
keytype first_key;
int k;
k = i+1;
first_key = a[i].key;
while( k<=j && a[k].key == first_key) // cac phan tu trung
	k++;
if(k>j)
	return -1;
else 
	if(a[k].key < first_key)
		return k;
	else 
		return i;
}
//phan hoach
int partition2(recordtype a[], int i, int j, keytype pivot) {
int L, R;
L = i;
R = j;
while(L<=R) {
	while(a[L].key <= pivot)
		L++;
	while(a[R].key > pivot) 
		R--;
	if(L<R)
		swap(&a[L],&a[R]);	
}
return L;
}
//thuat toan sap xep nhanh bien the
void quick_Sort2(recordtype a[], int i, int j) {
keytype pivot;
int pivot_idx, k;
pivot_idx = find_Pivot2(a, i ,j);
if(pivot_idx != -1) {
	pivot = a[pivot_idx].key;
	k = partition2(a, i ,j, pivot);
	quick_Sort2(a, i, k-1);
	quick_Sort2(a, k, j);
}
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
int n, i;
read_Data(a, &n);
printf("Du lieu truoc khi sap xep: \n");
print_Data(a, n);
printf("Chon thuat toan sap xep: \n");
printf("--------------------------------------------------------------------------------------------------\n");
printf("|\t1-Selection Sort\t | \t2-Bubble Sort\t\t| \t3-Insertion Sort\t |\n");
printf("--------------------------------------------------------------------------------------------------\n");
printf("|\t4-Quick Sort\t\t | \t5-Quick Sort Bien The\t|  \t6-Heap Sort\t\t |\n");
printf("--------------------------------------------------------------------------------------------------\n");
scanf("%d", &i);
while(i == 0 || i>6)
switch(i){
	case 1:	selection_Sort(a, n); break;
	case 2:	insertion_Sort(a, n); break;
	case 3:	bubble_Sort(a, n); break;
	case 4:	quick_Sort(a, 0, n-1); break;
	case 5:	quick_Sort2(a, 0, n-1); break;
	case 6:	heap_Sort(a, n); break;
	default: {
		printf("Nhap lai: \n");
		scanf("%d", &i);
	}
};
printf("Thuc hien thuat toan %s: \n", sort[i-1]);
printf("Du lieu sau khi sap xep: \n");
print_Data(a, n);
return 0;
}
