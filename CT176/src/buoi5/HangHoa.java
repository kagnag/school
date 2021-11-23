package buoi5;

import java.util.Scanner;

public class HangHoa {
	private String ms, ten;
	private Date ngaySX;
	
	public HangHoa() {
		ms = new String();
		ten = new String();
		ngaySX = new Date();
	}
	public HangHoa(HangHoa h) {
		this.ms = new String(h.ms);
		this.ten = new String(h.ten);
		this.ngaySX = new Date(h.ngaySX);
	}
	
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhap ma so hang hoa: ");
		ms = sc.nextLine();
		System.out.print("Nhap ten hang hoa: ");
		ten = sc.nextLine();
	}
	public void hienthi() {
		System.out.println("Ma so hang hoa: "+ ms + "\tTen hang hoa: "+ ten);
	}
}
