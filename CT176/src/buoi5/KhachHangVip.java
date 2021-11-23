package buoi5;

import java.util.Scanner;

public class KhachHangVip extends KhachHang {
	private float heso;
	private Date ngaytgia;
	
	public KhachHangVip() {
		super();
		heso = 0f;
		ngaytgia = new Date();
	}
	public KhachHangVip(KhachHang k,float heso, Date ngaytgia) {
		super(k);
		this.heso = heso;
		ngaytgia = new Date(ngaytgia);
	}
	public KhachHangVip(KhachHangVip v) {
		super(v);
		heso = v.heso;
		ngaytgia = new Date(v.ngaytgia);
	}
	
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		super.nhap();
		System.out.print("Nhap he so: ");
		heso = sc.nextFloat();
		System.out.print("Nhap ngay tham gia: ");
		ngaytgia.nhap();
	}
	
	public void hienthi() {
		super.hienthi();
		System.out.println("He so: " +heso+ "\tNgay tham gia: " +ngaytgia);
	}

}
