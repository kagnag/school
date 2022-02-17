package buoi2;

import java.util.Scanner;

public class Date {
	private int ngay, thang, nam;

	public Date() {
		ngay = 01;
		thang = 01;
		nam = 2000;
	}

	public Date(int d, int m, int y) {
		ngay = d;
		thang = m;
		nam = y;
	}
	
	public Date(Date d) {
		ngay = d.ngay;
		thang = d.thang;
		nam = d.nam;
	}
	
	public String toString() {
		return ngay + "/" + thang + "/" + nam;
	}

	public void hien() {
		System.out.println(ngay + "/" + thang + "/" + nam);
	}

	public void nhap() {
		Scanner sc = new Scanner(System.in);
		do {
/*			System.out.println("Nhap ngay"); */
			ngay = sc.nextInt();
/*			System.out.println("Nhap thang"); */
			thang = sc.nextInt();
/*			System.out.println("Nhap nam"); */
			nam = sc.nextInt();
		} while (!hople());
	}

	public boolean nhuan() {
		if ((nam % 4 == 0 && nam % 100 != 0) || nam % 400 == 0)
			return true;
		else
			return false;
	}

	public boolean hople() {
		int max[] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
		if (nhuan() == true) {
			max[2] = 29;
		}
		if (ngay > 0 && thang > 0 && nam > 0 && thang < 13 && ngay <= max[thang]) {
			return true;
		} else
			return false;
	}

	public Date ngayHomSau() {
		Date d = new Date(ngay, thang, nam);
		d.ngay++;
		if (!d.hople()) {
			d.ngay = 1;
			d.thang++;
		}
		if (!d.hople()) {
			d.thang = 1;
			d.nam++;
		}
		return d;
	}

	public Date congNgay(int n) {
		Date d = new Date(ngay, thang, nam);
		for (int i = 0; i < n; i++) {
			d = d.ngayHomSau();
		}
		return d;
	}

	public int SoSanh(Date d) {
		if (nam > d.nam)
			return 1;
		else if (nam < d.nam)
			return -1;
		else if (thang > d.thang)
			return 1;
		else if (thang < d.thang)
			return -1;
		else if (ngay > d.ngay)
			return 1;
		else if (ngay < d.ngay)
			return -1;
		else
			return 0;
	}
}
