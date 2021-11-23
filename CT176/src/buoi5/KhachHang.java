package buoi5;

import java.util.Scanner;
public class KhachHang {
	private String ms, ten, dc;
	public KhachHang() {
		ms = new String();
		ten = new String();
		dc = new String();
	}
	public KhachHang(String ms, String ten, String dc) {
		this.ms = new String(ms);
		this.ten = new String(ten);
		this.dc = new String(dc);
	}
	public KhachHang(KhachHang k) {
		ms = new String(k.ms);
		ten = new String(k.ten);
		dc = new String(k.dc);
	}
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap thong tin khach hang");
		System.out.print("Nhap ma so: ");
		ms = sc.nextLine();
		System.out.print("Nhap ten: ");
		ten = sc.nextLine();
		System.out.print("Nhap dia chi: ");
		dc = sc.nextLine();
	}
	public void hienthi() {
		System.out.println("Thong tin khach hang");
		System.out.println("Ma so: " +ms+ "\t Ten: " +ten+ "\nDia chi: " +dc);
	}
}
