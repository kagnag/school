package buoi2;

import java.util.Scanner;

public class SDDate {

	public static void main(String[] args) {
		int n, i;
		Scanner sc = new Scanner(System.in);
		Date d = new Date();
		d.nhap();
		d.hien();
		System.out.println("Nhap so ngay cong them");
		n = sc.nextInt();
		d=d.congNgay(n);
		d.hien();
		
		Date ds[];
		System.out.println("Nhap so date");
		int t = sc.nextInt();
		ds = new Date[t];
		for(i = 0; i < t; i++) {
			ds[i]=new Date();
			System.out.println("Nhap Date thu " + (i+1));
			ds[i].nhap();
		}
		Date max = new Date(1,1,1);
		for(Date a:ds)
			if(a.SoSanh(max) > 0)
				max=a;
		System.out.println("Ngay gan nhat; ");
		max.hien();
		
		
	}

}
