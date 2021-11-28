// Bai toan ma tran so

#include<stdio.h>

#define size 50

void read_data(int a[][50], int n, int m){
	FILE *f;
	f=fopen("ma_tran_so.txt", "r");
	if(f==NULL){
		printf("File loi!!!");
		return;
	}
	int i, j;
	while(!feof(f)){
		for (i=0; i<n; i++)
			for (j=0; j<m; j++)
				fscanf(f, "%d", &a[i][j]);
	}
	fclose(f);
}

void print_data(int a[][size], int n, int m) {
    int i, j;
    printf("\nMa tran so da cho\n");
    for(i = 0; i<n; i++) {
        for(j = 0; j<m; j++) 
            printf("%5d", a[i][j]);
        printf("\n");
    }
}

int cs_max(int F[][size], int i, int j) {
    if(j == 0)
        return (F[i-1][0] > F[i-1][1]) ? 0 : 1;
    if(j == 1)
        return i - 1;
    if(j == i-1)
        return (F[i-1][i-2] > F[i-1][i-1]) ? i-2 : i-1;
    if(F[i-1][j-1] > F[i-1][j] && F[i-1][j-1] > F[i-1][j+1])
        return j - 1;
    if(F[i-1][j] > F[i-1][j-1] && F[i-1][j] > F[i-1][j+1])
        return j;
    if(F[i-1][j+1] > F[i-1][j] && F[i-1][j+1] > F[i-1][j-1])
        return j+1;
}

void tao_bang(int a[][size], int n, int m, int F[n][m]) {
    int i, j;
    // moi phan tu cua bang F duoc xac dinh nho vao dong truoc do (truy hoi)
    for(i = 0; i<n; i++) 
        for(j = 0; j<m; j++){
            int k = cs_max(F, i, j);
            F[i][j] = F[i-1][k] + a[i][j];
        }
}

void in_bang(int n, int m, int F[n][m]) {
    int i, j;
    printf("\nBang F\n");
    for(i = 0; i<n; i++) {
        for(j = 0; j<m; j++) 
            printf("%5d", F[i][j]);
        printf("\n");
    }
}

int cs_max_dong_cuoi(int F[], int j) {
    int somax = F[0];
    int maxindex = 0;
    int k;
	for(k = 1; k<=j; k++)
		if(F[k] > somax) {
			somax = F[k];
			maxindex = k;
		}
	return maxindex;
}

// Tra bang F nhung xac dinh phuong an tu trong ma tran so (bang a)

void tra_bang(int a[][size], int n, int F[][size], int PA[]) {
	int i, j;
	// Xac dinh chi so j cua phan tu lon nhat o dong cuoi trong bang F
	j = cs_max_dong_cuoi(F[n-1], n-1);
	
	// Phan ti cuoi cung cua duong di tuc la PA[n-1]
	// la phan tu cua dong cuoi cung bang a, ung voi cot j vua tim thay o tren
	PA[n-1] = a[n-1][j];
	
	// Xet cac dong cua bang F, tu dong n-1 den dong 1
	// De xac dinh cac phan tu cua PA tu PA[n-2] den PA[0]
	
	for(i = n-1; i>=1; i--) {
		
		// Can cu vao chi so cot j cua dong cuoi (dong i) cua bang F
		// ma xac dinh chi so cot j cua dong tren (dong i - 1) cua bang F
		 j = cs_max(F, i ,j);
		 
		// PA[i-1] la phan tu cua dong i - 1 cua ma tran so a,
		// ung voi cot j vua tim thay o tren
		
		PA[i-1] = a[i-1][j];
	}
}

int gia_PA(int PA[], int n) {
	int i;
	int sum = 0;
	for(i = 0; i<n; i++)
		sum += PA[i];
	return sum;
}

void printPA(int PA[], int n) {
	int i;
	printf("\nPhuong an la duong di qua cac so: ");
	printf("\%d", PA[0]);
	for(i = 1; i<n; i++)
		printf(" => %d", PA[i]);
	printf("\n\nTong cac so tren duong di la %d\n", gia_PA(PA, n));	
}

int main() {
	int a[size][size]; 		
	int n = 4, m = 5;
	
	printf("\nBai toan Ma tran so dung thuat toan Quy hoach dong\n");
	read_data(a, n, m);
	print_data(a, n, m);
	
	int PA[n]; 		// Phuong an toi uu: mang n co n phan tu
	int F[n][n];		// Bang F: mang 2 chieu co n dong, n cot
	
	tao_bang(a, n, m, F);
	in_bang(n, m, F);
	
	tra_bang(a, n, F, PA);
	printPA(PA, n);
}










