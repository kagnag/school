package buoi5;

import java.util.Scanner;

public class ChiTiet {
	private int soLuong;
	private long donGia;
	private HangHoa h;
	
	public ChiTiet() {
		soLuong = 0;
		donGia = 0;
		h = new HangHoa();
	}
	public ChiTiet(int sl, long dg, HangHoa h) {
		soLuong = sl;
		donGia = dg;
		this.h = h;
	}
	public ChiTiet(ChiTiet C) {
		soLuong = C.soLuong;
		donGia = C.donGia;
		h = new HangHoa(C.h);
	}
	
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhap so luong va don gia: ");
		soLuong = sc.nextInt();	
		donGia = sc.nextLong();
		System.out.println("Nhap hang hoa: ");
		h.nhap();
	}
	public void hienthi() {
		System.out.println("So luong hang hoa: " + soLuong + "\tDon gia: " + donGia);
		h.hienthi();
	}
}
