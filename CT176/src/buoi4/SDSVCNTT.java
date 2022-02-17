package buoi4;
import java.util.Scanner;
import buoi3.SinhVien;
public class SDSVCNTT {
	public static void main(String[] args) {
		SinhVienCNTT sv = new SinhVienCNTT();
		SinhVien ds[];
		Scanner sc = new  Scanner(System.in);
		int n;
		System.out.println("Nhap so sinh vien: ");
		n = sc.nextInt();
		sc.nextLine();
		char c;
		ds = new SinhVien[n];
		for(int i = 0; i < n; i++) {
			boolean tr = false;
			do{
				System.out.println("Nhap thong tin cho sinh vien (s),"
						+ " cho sinh vien CNTT (c): ");
				c = sc.nextLine().charAt(0);
				if(c != 's' && c!= 'c') {
					System.out.println("Chi nhap (s) va (v).\nNhap lai:");
					tr = true;
				}
				else break;
			}while(tr = true);
			if(c == 's') 
				ds[i] =  new SinhVien();
			else if(c == 'c')
				ds[i] = new SinhVienCNTT();
			ds[i].nhap();
		}
		for(int i = 0; i < n; i++)
			System.out.println("Sinh vien thu " + (i+1) + ": " + ds[i]);

		System.out.println("Nhap thong tin sinh vien can tim: ");
		sc.nextLine();
		String email = sc.nextLine();
		for(int i = 0; i < n; i++) {
			if((ds[i]).getEmail().equals(email)) {
				System.out.println("Email: "+ email + "\n" + ds[i].toString() +" "+ ds[i].getEmail());
				break;
			}
			else
				System.out.println("Email khong co trong danh sach sinh vien");
			break;
		}

	}

}
