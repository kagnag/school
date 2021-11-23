package buoi3;
import buoi2.Date;
import java.util.Scanner;
public class SinhVien {
	private String mssv, hoTen;
	private Date nSinh;
	private int sl;
	private String tenHP[], Diem[];
	public SinhVien() {
		mssv = new String();
		hoTen = new String();
		nSinh = new Date();
		sl = 0;
		tenHP = new String[50];
		Diem = new String[50];
	}
	public SinhVien(SinhVien S) {
		mssv = new String(S.mssv);
		hoTen = new String(S.hoTen);
		nSinh = new Date(S.nSinh);
		sl = S.sl;
		for(int i=0; i<sl; i++) {
			tenHP[i] = new String(S.tenHP[i]);
			Diem[i] = new String(S.Diem[i]);
		}
	}

	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap ma so sinh vien");
		mssv = sc.nextLine();
		System.out.println("Nhap ho ten sinh vien");
		hoTen = sc.nextLine();
		System.out.println("Nhap ngay sinh cua sinh vien");
		nSinh.nhap(); 
	}

	public void nhapDiemHP() {
		Scanner sc = new Scanner(System.in);
		for(int i=0; i<sl ;i++) {
			System.out.println("Nhap diem hoc phan thu " + tenHP[i]);
			Diem[i] = sc.nextLine();
		}
	}

	public void dkHP() {
		Scanner sc = new Scanner(System.in);
			System.out.println("Nhap so hoc phan dang ky");
		sl = sc.nextInt();
		sc.nextLine();
		for(int i=0; i<sl; i++) {
			System.out.println("Nhap ten hoc phan thu " + (i+1) + ":");
			tenHP[i] = sc.nextLine();
		}
	}
	
	public String toString() {
		String S = mssv + ", " + hoTen + ", " + nSinh;
		for(int i=0; i<sl ; i++)
			S += " " + tenHP[i] + ":" + Diem[i];	
		return S;
	}

	public float DTB() {
		float dtb=0.0f;
		for(int i = 0; i< sl; i++) {
			switch(Diem[i]){
			case "A":
				dtb += 4.0f;
			case "B+":
				dtb += 3.5f;
			case "B":
				dtb += 3.0f;
			case "C+":
				dtb += 2.5f;
			case "C":
				dtb += 2.0f;
			case "D+":
				dtb += 1.5f;
			case "D":
				dtb += 1.0f;
			}
		}  dtb=dtb/sl;	
		return dtb;
	}

	public void themHP(String ten, String d) {
		if(sl < tenHP.length-1);
		tenHP[sl] = new String(ten);
		Diem[sl] = new String(d);
		sl++;
	}

	public void xoaHP(String ten) {
		int pos = -1;
		for(int i=0; i <sl; i++) {
			if(tenHP[i].equals(ten)) {
				pos = i; 
				break;
			}
			if( pos != -1) {
				for( i = pos; i<sl; i++) {
					tenHP[i] = tenHP[i+1];
					Diem[i] = Diem[i+1];
				}
			}
			sl--;
		}
	}

	public String layTen() {
		String h = new String(hoTen);
		h = h.trim();
		return h.substring(h.lastIndexOf(" ") + 1);
	}
	
	public String getEmail() {
		return " ";
	}
}
