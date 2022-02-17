package buoi5; 

import java.util.Scanner;

public class BanHang {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		HoaDon hd = new HoaDon();
		//HoaDon ds[];
		KhachHang k =  new KhachHang();
		KhachHang q[];	
		int n;
		System.out.print("Nhap so khach hang: ");
		n = sc.nextInt();
		sc.nextLine();
		q = new KhachHang[n];
		//ds = new HoaDon[n];
		char a;
		for(int i = 0; i< n; i++) {
			boolean tr = false;
			do { 
				System.out.println("Nhap thong tin khach hang pho thong(n),"
						+ " khach hang Vip(v)");
				a = sc.nextLine().charAt(0);
				if(a != 'n' && a != 'v') {
					System.out.println("Chi nhap (n) hoac (v).\nNhap lai!");
					tr = true;
				}
				else break;
			}while(tr = true);
				if(a == 'n') 
					q[i] =  new KhachHang();		
				else if(a == 'v') 
					q[i] = new KhachHangVip();
						q[i].nhap();
						hd.nhap();
						q[i].hienthi();
						hd.hienthi();		
}
}
}
