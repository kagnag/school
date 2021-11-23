package buoi3;

import buoi2.Diem;

public class DoanThang {
	private Diem A, B;
	public DoanThang() {
		A = new Diem();
		B= new Diem();
	}
	public DoanThang(Diem A1, Diem B2) {
		A = new Diem(A1);
		B = new Diem(B2);
	}
	public DoanThang(int x1, int y1, int x2, int y2) {
		A = new Diem(x1,y1);
		B = new Diem(x2,y2);
	}
	public DoanThang(DoanThang dt) {
		A = new Diem(dt.A);
		B = new Diem(dt.B);
	}

	public void nhap() {
		System.out.println("Nhap toa do diem dau: ");
		A.nhapDiem();
		System.out.println("Nhap toa do diem cuoi: ");
		B.nhapDiem();
	}

	public String toString() {
		return "[" + A + "," + B + "]";
	}

	public void tinhTien(int dx, int dy) {
		A.doiDiem(dx, dy);
		B.doiDiem(dx, dy);
	}

	public float doDai() {
		return A.khoangCach(B);
	}

	/*	public void gocVoiX()
	 */
}	
