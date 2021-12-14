// Huynh Bao Khang
// b1913306

// bai toan ma tran so
# include<stdio.h>

# define col 4
# define row 5

void read_data(int a[col][row], int n, int m) {
	FILE * f;
	f = fopen("ma_tran_so.txt", "r");
	if(f==NULL) {
		printf("File loi!");
		return;
	}
	int i, j;
	while(!feof(f)){
		for(i = 0; i<n; i++)
			for(j = 0; j<m; j++)
				fscanf(f, "%d", &a[i][j]);
	}
	fclose(f);
}

void print_data(int a[col][row], int n, int m){
	int i, j;
	printf("\n Ma tran so da cho \n");
	for(i = 0; i<n; i++) {
		for(j = 0; j<m; j++)
			printf("%5d", a[i][j]);
		printf("\n");
	}
}

int cs_max(int F[col][row], int i, int j) {
	if(j == 0)
		return (F[i-1][0] > F[i-1][1]) ? 0 : 1;
	if(j == 1) 
		return i - 1;
	if(j == i - 1)
		return (F[i-1][i-2] > F[i-1][i-1]) ? i-2 : i-1;
	if(F[i-1][j-1] > F[i-1][j] && F[i-1][j-1] > F[i-1][j+1])
		return j - 1;
	if(F[i-1][j] > F[i-1][j-1] && F[i-1][j] > F[i-1][j+1])
		return j;
	if(F[i-1][j+1] > F[i-1][j] && F[i-1][j+1] > F[i-1][j-1])
		return j+1;
}

int tao_bang(int a[col][row], int n, int m, int F[n][m]) {
	int i, j;
	for(i = 0; i<n;  i++)
		for(j = 0; j<m; j++) {
			int k = cs_max(F, i , j);
			F[i][j] = F[i-1][k] + a[i][j];
		}
}

int in_bang(int n, int m, int F[n][m]) {
	int i, j;
	printf("\nBang F\n");
	for(i = 0; i<n; i++){
		for(j = 0; j<m; j++)
			printf("%5d", F[i][j]);
		printf("\n");
	}	
}

int cs_max_dong_cuoi(int F[], int j) {
	int somax = F[0];
	int maxindex = 0;
	int k;
	for(k = 1; k <= j; k++) 
		if(F[k] > somax) {
			somax = F[k];
			maxindex = k;
		}
	return maxindex;
}

void tra_bang(int a[col][row], int n, int F[col][row], int PA[]) {
	int i, j;
	j = cs_max_dong_cuoi(F[n-1], n-1);
	
	PA[n-1] = a[n-1][i];
	
	for(i = n-1; i>=1; i--) {
		j = cs_max(F, i, j);
		PA[i-1] = a[i-1][j];
	}
}

int gia_PA(int PA[], int n) {
	int i;
	int sum = 0;
	for(i = 0; i < n ; i++) 
		sum += PA[i];
	return sum;
}

void print_PA(int PA[], int n) {
	int i;
	printf("\nPhuong an la duong di qua cac so: ");
	printf("%d", PA[0]);
	for( i = 1; i<n; i++)
		printf(" => %d", PA[i]);
	printf("\nTong cac so tren duong di la %d\n", gia_PA(PA, n));
}

int main() {
	int a[col][row];
	int n = col, m = row;
	printf("\nBai toan Ma Tran So dung thuat toan QUY HOACH DONG\n");
	read_data(a, n, m);
	print_data(a, n, m);
	
	int PA[n];
	int F[n][m];
	
	tao_bang(a, n, m ,F);
	in_bang(n, m, F);
	
	tra_bang(a, n, F, PA);
	print_PA(PA, n);
	return 0;
}














