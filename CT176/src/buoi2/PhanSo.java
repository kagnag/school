package buoi2;

import java.util.Scanner;

public class PhanSo {
	private int tu, mau;

	public PhanSo() {
		tu = 0;
		mau = 1;
	}

	public PhanSo(int tu1, int mau1) {
		tu = tu1;
		mau = mau1;
	}

	public void nhap() {
		Scanner sc = new Scanner(System.in);
		do {
			System.out.println("Nhap tu so");
			tu = sc.nextInt();
			System.out.println("Nhap mau so");
			mau = sc.nextInt();
		} while (mau != 0);
	}

	public void in() {
		if (tu == 0) {
			System.out.println("0");
		} else if (mau == 1) {
			System.out.println(tu);
		} else
			System.out.println(tu + "/" + mau);
	}

	public void nghichDao() {
		int temp = 0;
		tu = temp;
		mau = tu;
		temp = mau;
	}
	
/*	public PhanSo giaTriNghichDao() {
		PhanSo t = new PhanSo(tu, mau);
		t = x;
		t.nghichDao();
	} */

	public float giaTri() {
		float gt;
		return gt = (float) tu / mau;
	}

/*	public boolean lonHon(PhanSo a) {
		if ( a.giaTri > a.giaTri())
			return true;
		else
			return false;
	}	*/
}
