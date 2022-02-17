package buoi2;

import java.util.Scanner;
public class SDDiem {

	public static void main(String[] args) {
		Diem A;
		A = new Diem(3,4);
		System.out.println("Toa do diem A");
		A.hienThi();
		Diem B;
		B = new Diem();
		B.nhapDiem();
		System.out.println("Toa do diem B");
		B.hienThi();
		Diem C;
		C = new Diem(-B.giaTriX(),-B.giaTriY());
		System.out.println("Toa do diem C");
		C.hienThi();
		System.out.println("BO = "+ B.khoangCach());
		System.out.println("AB = "+ B.khoangCach(A));
		
			Diem ds[];
			Scanner sc = new Scanner(System.in);
			System.out.println("Nhap so diem");
			int n = sc.nextInt();
			ds = new Diem[n];
			for (int i=0; i<n; i++) {
				System.out.println("Nhap diem thu " + (i+1) + ":" );
				ds[i]=new Diem();
				ds[i].nhapDiem();
			}
			for(Diem d:ds)
				d.hienThi();
	}

}
