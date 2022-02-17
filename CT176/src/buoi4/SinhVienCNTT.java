package buoi4;
import java.util.Scanner;
import buoi3.SinhVien;

public class SinhVienCNTT extends SinhVien{
	private String taikhoan;
	private String matkhau;
	private String email;

	public SinhVienCNTT() {
		super();
		taikhoan = new String();
		matkhau = new String();
		email = new String();
	}
	public SinhVienCNTT(SinhVienCNTT S) {
		super((SinhVien) S);
		this.taikhoan = new String(S.taikhoan);
		this.matkhau = new String(S.matkhau);
		this.email = new String(S.email);
	}

	public void nhap() {
		super.nhap();
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap tai khoan: ");
		taikhoan = sc.nextLine();
		System.out.println("Nhap mat khau: ");
		matkhau = sc.nextLine();
		System.out.println("Nhap email");
		email = sc.nextLine();	
	}
	
	public String toString() {
		return super.toString() + "\ntai khoan: " + taikhoan 
				+ "\nmat khau: " + matkhau + "\nemail: " + email;
	}
	
	public String getEmail() {
		return email;
	}
	
	public void doiMatKhau(String newpass) {
		matkhau = new String(newpass);
	}
}

