package buoi5;

import java.util.Scanner;
public class HoaDon {
	private String ms, tenCH;
	private ChiTiet c[];
	private Date ngayLap;
	private int sl;
	//private KhachHang k;
	
	public HoaDon() {
		ms = new String();
		tenCH = new String();
		c = new ChiTiet[100];
		ngayLap = new Date();
		for(int i = 0; i< 100; i++) {
			c[i] = new ChiTiet();
		}
	//	k = new KhachHang();
	}
	public HoaDon(String ms, String tenCH, ChiTiet c[], Date ngaylap, KhachHang k) {
		this.ms = new String(ms);
		this.tenCH = new String(tenCH);
		this.c = new ChiTiet[c.length];
		this.ngayLap = new Date(ngayLap);
		for(int i = 0; i< c.length; i++) {
			this.c[i] = new ChiTiet();
		}
	//	this.k = new KhachHang(k);
	}		
	public HoaDon(HoaDon h) {
		ms = new String(h.ms);
		tenCH = new String(h.tenCH);
		c = new ChiTiet[h.c.length];
		ngayLap = new Date(h.ngayLap);
		for(int i = 0; i< h.c.length; i++) {
			c[i] = new ChiTiet(h.c[i]);
		}
	//	k = new KhachHang(h.k);
	}
	
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhap ten Cua Hang: ");
		tenCH = sc.nextLine();
		System.out.print("Nhap ma so hoa don: ");
		ms = sc.nextLine();
		System.out.print("Nhap ngay lap hoa don: ");{
		ngayLap.nhap();
		System.out.print("Nhap so luong don hang: ");
		int sl;
		sl = sc.nextInt();
		c = new ChiTiet[sl];
		for(int i = 0; i< sl; i++) {
			c[i] = new ChiTiet();
			System.out.println("Nhap don hang thu "+ (i+1) + " ");
			c[i].nhap();
		}
		}
	}
	public void hienthi() {
		System.out.println("Ten Cua Hang: " +tenCH+ "\nMa so hoa don: " +ms+ "\tNgay lap: " +ngayLap);
		for(int i =0; i< c.length; i++) {
			c[i].hienthi();
	}
}
}
