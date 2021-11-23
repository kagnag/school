package buoi3;

import buoi2.Diem;

public class SDDoanThang {

	public static void main(String[] args) {
	Diem A = new Diem(2,5);
	Diem B = new Diem(20,35);
	DoanThang AB = new DoanThang(A, B);
	System.out.println("AB: " +AB);
	System.out.println("Tien tien doan thang AB mot doan (3,5)");
	AB.tinhTien(3, 5);
	System.out.println("AB: " +AB);
	DoanThang CD = new DoanThang();
	CD.nhap();
	System.out.println("CD: " +CD);
	System.out.println("Do dai cua doan thang CD: " + CD.doDai() );
	}

}
