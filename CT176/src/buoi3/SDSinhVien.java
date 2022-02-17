package buoi3;
import java.util.Scanner;
public class SDSinhVien {

	public static void main(String[] args) {
		
	SinhVien a = new SinhVien();
		a.nhap();
		System.out.println("Them hoc phan LTHDT voi diem F");
		a.themHP("LTHTD","F");
		System.out.println("Sinh vien a: " +a); 
		SinhVien ds[];
		Scanner sc = new Scanner(System.in);

		int n;
		System.out.println("Nhap so sinh vien");
		n = sc.nextInt();
		ds = new SinhVien[n];
		for(int i=0; i<n; i++){
			ds[i] = new SinhVien();
		}
		for(int i=0; i<n; i++) {
			System.out.println("Nhap thong tin Sinh Vien thu " + (i+1)+ ":");
			ds[i].nhap();
			ds[i].dkHP();
			ds[i].nhapDiemHP();
		}
		for(int i=0; i>n; i++) {
			System.out.println("Thong tin Sinh Vien thu" + (i+1) + ds[i]);
		}

		System.out.println("Danh sach sinh vien bi canh cao hoc vu: ");
		for(int i=0; i<n; i++) {
			if(ds[i].DTB()<1)
				System.out.println(ds[i]);
		}

		int svmax = 0;
		float maxDTB=0.0f;
		for(int i=0; i<n; i++) {
			maxDTB=Math.max(ds[i].DTB(), maxDTB);
			svmax = i;
			}
			System.out.println("Sinh vien co diem trung binh cao nhat lop: " + ds[svmax].toString() + " " + maxDTB);	
		
		System.out.println("Danh sach sinh vien theo thu thu ALphabet cua Ten");
		for(int i=0; i<n-1 ; i++) {
			for(int j=i+1; j<n; j++) {
				if(ds[i].layTen().compareTo(ds[j].layTen()) >0) {
					SinhVien t = ds[i];
					ds[i] = ds[j];
					ds[j] = t;
				}
			}				
		}
		for(int i=0; i<n; i++) {
			System.out.println("Thong tin sinh vien thu "+ (i+1) + ": " + ds[i]);
		}
	}

}
