// HUynh Bao Khang
// B1913306
#include<stdio.h>
#include<malloc.h>
#include<string.h>

typedef struct {
    char TenDV[20];
    float TL, GT, DG;
    int SL, PA;
}DoVat;

DoVat * read_from_file(float *W, int *n) {
    FILE *f;
    f = fopen("cai_ba_lo_2.txt", "r");
    fscanf(f, "%f", W); // xac dinh trong luong balo
    DoVat *dsdv;
    dsdv = (DoVat*)malloc(sizeof(DoVat));
    int i = 0;
    while (!feof(f)) {
        fscanf(f,"%f %f %d %[^\n]", &dsdv[i].TL, &dsdv[i].GT, &dsdv[i].SL, &dsdv[i].TenDV);
        dsdv[i].DG = dsdv[i].GT / dsdv[i].TL;
        dsdv[i].PA = 0;
        i++;
        dsdv = (DoVat*)realloc(dsdv, sizeof(DoVat)*(i+1));
    }
    *n = i;
    fclose(f);
    return dsdv;
}

void swap(DoVat *x, DoVat *y) {
    DoVat temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

void bubble_sort(DoVat *dsdv, int n) {
    int i, j;
    for(i = 0; i<n-2; i++) 
        for(j = n-1; j>=i+1; j--) {
            if(dsdv[j].DG > dsdv[j-1].DG)
                swap(&dsdv[j], &dsdv[j-1]);
        }
}

void in_dsdv(DoVat *dsdv, int n, float W) {
    int i;
    float tong_tl = 0.0, tong_gt = 0.0;
    printf("\nPhuong an Cai ba lo 2 dung thuat toan Nhanh Can:\n");
    printf("\nTrong luong cua ba lo = %-9.2f\n", W);
    printf("STT     Ten Do Vat              T.Luong     Gia Tri     So Luong    Don Gia     Phuong An\n");
    for(i = 0; i<n; i++) {
        printf("%2d\t %-20s %10.2f %10.2f %10d %10.2f %10d\n", 
        i+1, dsdv[i].TenDV, dsdv[i].TL, dsdv[i].GT, dsdv[i].SL, dsdv[i].DG, dsdv[i].PA);
        tong_tl = tong_tl + dsdv[i].PA * dsdv[i].TL;
        tong_gt = tong_gt + dsdv[i].PA * dsdv[i].GT;
    }
    printf("\n");
    printf("Phuong an (theo thu tu DG giam dan): X(");
    for(i = 0; i<n-1; i++) 
        printf("%d,", dsdv[i].PA);
    printf("%d)", dsdv[n-1].PA);
    printf("\nTong trong luong = %-9.2f\n", tong_tl);
    printf("Tong gia tri = %-9.2f\n", tong_gt);
}

// Tinh cac dai luong tai nut goc
void tao_nut_goc(float W, float *V, float *CT, float *GLNTT, float *TGT, float DG_Max) {
    *TGT = 0.0;
    *V = W;
    *CT = *V * DG_Max;
    *GLNTT = 0.0;
}

// Ghi nhan phuong an tot nhat tam thoi
void cap_nhat_GLNTT(float TGT, float *GLNTT, int x[], DoVat *dsdv, int n) {
    int i;
    if(*GLNTT < TGT) {
        *GLNTT = TGT;
        for(i = 0; i<n; i++)
            dsdv[i].PA = x[i];
    }
}

int min(int a, int b) {
    return a < b ? a : b;
}

void nhanh_can(int i, float *TGT, float *CT, float *V, float *GLNTT, int x[], DoVat *dsdv, int n) {
    int j;      // j la so vat duoc chon
    int yk;     // so do vat lon nhat co the chon
    yk = min(dsdv[i].SL, *V / dsdv[i].TL);
    for(j = yk; j>= 0; j--) {       //xet tat ca kha nag co the phan nhanh theo so luong do vat
        // ung voi mot gia tri cua j la mot nut tren cay
        // tinh 3 dai luong cua mot nut trong
        *TGT = *TGT + j*dsdv[i].GT;
        *V = *V - j*dsdv[i].TL;
        *CT = *TGT + *V * dsdv[i+1].DG;  //dsdv[i].DG la DG vat ke tiep cua vat i (i + 1)
        if(*CT > *GLNTT) {      // truong hop chua cat tia (dieu kien cat tia la khi CT <= GLNTT)
            x[i] = j;
            if((i == n-1) || (*V == 0)) // da xet het tat ca cac do vat hoac ba lo da day
                cap_nhat_GLNTT(*TGT, GLNTT, x, dsdv, n);
            else 
                nhanh_can(i+1, TGT, CT, V, GLNTT, x, dsdv, n);
        }
    // quay lui xet nut khac
    x[i] = 0;
    *TGT = *TGT - j*dsdv[i].GT; // tra lai tong gia tri cua nut cha
    *V = *V + j*dsdv[i].TL;     // tra lai trong luong con lai cua nut cha
    }
}

int main() {
    DoVat *dsdv;
    int n;
    float W;
    float CT; 
    float TGT;
    float V;
    float GLNTT;
    
    dsdv = read_from_file(&W, &n);
    int x[n];

    bubble_sort(dsdv, n);
    tao_nut_goc(W, &V, &CT, &GLNTT, &TGT, dsdv[0].DG);
    nhanh_can(0, &TGT, &CT, &V, &GLNTT, x, dsdv, n);
    in_dsdv(dsdv, n, W);
    free(dsdv);
    return 0;
}