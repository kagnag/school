// Huynh Bao Khang
// B1913306

#include<stdio.h>
#include<malloc.h>
#include<string.h>

typedef struct {
	char TenDV[20];
	int TL, GT, SL, DG, PA;
}DoVat;


typedef int bang[100][100]; 	
DoVat *read_from_file(int *W, int *n) {
	FILE *f;
	f = fopen("QHD_cai_ba_lo2.txt", "r");
	fscanf(f, "%d", W); 	// xac dinh trong luong ba lo
	DoVat *dsdv;
	dsdv = (DoVat*)malloc(sizeof(DoVat));
	int i = 0;
	while (!feof(f)) {
		fscanf(f, "%d %d %d %[^\n]", 
		&dsdv[i].TL, &dsdv[i].GT, &dsdv[i].SL, &dsdv[i].TenDV);
		dsdv[i].DG = dsdv[i].GT / dsdv[i].TL;
		dsdv[i].PA = 0;
		i++;
		dsdv = (DoVat*)realloc(dsdv, sizeof(DoVat)*(i+1));
	}
	*n = i;
	fclose(f);
	return dsdv;
}

void in_dsdv(DoVat *dsdv, int n, int W) {
	int i, tong_tl = 0, tong_gt = 0;
	printf("Phuong an cai ba lo 2 dung thuat toan Quy Hoach Dong nhu sau:\n");
	printf("Trong luong cua ba lo = %-10d\n", W);
	printf("\nSTT	Ten Do Vat		T Luong		Gia Tri		So Luong	Don Gia		Phuong An\n");
	for(i = 0; i<n; i++) {
		printf("%2d\t %-20s %5d %15d %15d %15d %15d\n",
		i+1, dsdv[i].TenDV, dsdv[i].TL, dsdv[i].GT, dsdv[i].SL, dsdv[i].DG, dsdv[i].PA);
		tong_tl = tong_tl + dsdv[i].PA * dsdv[i].TL;
		tong_gt = tong_gt + dsdv[i].PA * dsdv[i].GT;
	}
	printf("\nPhuong an (theo thu tu DG giam dan): X(");
	for(i = 0; i<n-1; i++)
		printf("%d, ", dsdv[i].PA);
	printf("%d)", dsdv[n-1].PA);
	printf("\nTong trong luong = %-10d\n", tong_tl);
	printf("Tong gia tri = %-10d", tong_gt);	
}

int min(int a, int b) {
	return a < b ? a : b;
}

void tao_bang(DoVat *dsdv, int n, int W, bang F, bang X) {
	int xk, yk, k;
	int FMax, XMax, V;
	// dien dong dau tien cua hai bang
	for(V = 0; V<=W; V++) {
		X[0][V] = V / dsdv[0].TL;
		F[0][V] = X[0][V] * dsdv[0].GT;
	}
	// dien cac dong con lai
	for(k = 1; k<n; k++) {
		for(V = 0; V<=W; V++) {
			FMax = F[k-1][V];
			XMax = 0;
			yk = min(V / dsdv[k].TL, dsdv[k].SL);
			for(xk = 1; xk<=yk; xk++) 
				if(F[k-1][V-xk*dsdv[k].TL] + xk*dsdv[k].GT > FMax) {
					FMax = F[k-1][V-xk*dsdv[k].TL] + xk*dsdv[k].GT;
					XMax = xk;
				}
			F[k][V] = FMax;
			X[k][V] = XMax;
		}
	}
}

void in_bang(int n, int W, bang F, bang X) {
	int V, k;
	printf("\nBang F|X \n");
	printf("  |\t0 | \t1 | \t2 |\t3 | \t4 | \t5 | \t6 | \t7 | \t8 | \t9 |\n");
	for(k = 0; k<n; k++) {
		printf("%2d|", k+1);
		for(V = 0; V<=W; V++)
			printf("%3d %2d |", F[k][V], X[k][V]);
		printf("\n");
	}
}

void tra_bang(DoVat *dsdv, int n, int W, bang X) {
	int k, V;
	V = W;
	for(k = n-1; k>=0; k--) {
		dsdv[k].PA = X[k][V];
		V = V - X[k][V] * dsdv[k].TL;
	}
}

int main() {
	int n, W;
	bang X, F;
	DoVat *dsdv;
	dsdv = read_from_file(&W, &n);
	tao_bang(dsdv, n, W, F, X);
	in_bang(n, W, F, X);
	printf("\n");
	tra_bang(dsdv, n, W, X);
	in_dsdv(dsdv, n, W);
	free(dsdv);
	return 0;
}
