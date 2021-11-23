package buoi3;

import java.util.Scanner;

public class SDGach {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Gach ds[];
		int n;
		
		System.out.println("Nhap vao so hop gach ");
		n = sc.nextInt();
		ds = new Gach[n];
		for(int i = 0; i<n ; i++) {
			ds[i] = new Gach();
		}
		
		for(int i = 0; i < n; i++	) {
			System.out.println("Nhap thong tin hop gach " +  (i+1) + ":");
			ds[i].nhap();
		}
		
		for(int i = 0; i < n; i++) {
			ds[i].in();
		}
		
		float payMin = 0;
		String mGach = null;
		for(int i = 0; i < n - 1 ; i++) {
			if( ds[i].cpThap() > ds[i+1].cpThap() ) {
				payMin = ds[i+1].cpThap();	
				mGach = ds[i+1].layMS();
			}
		}
		
		System.out.println("Loai gach co chi phi lot thap nhat la " + mGach + " voi gia/dt "+ payMin);
		
		System.out.println("So tien it nhat cho 1 dien tich dai 20m ngang 5m ");
			long min = Long.MAX_VALUE;	
			for(int i = 0; i<n;       i++) {
				long t = ds[i].SoHopMin(20,5)*ds[i].layGia();
				if(t<min) 
					min = t;
		} 
		System.out.println(min);
	
		for(int i =0; i < n; i++) {
			System.out.println("So tien khi lot cho 1 dien tich dai 20m ngang 5m voi loai gach "+ ds[i].layMS() + " voi gia" + ds[i].layGia() + "\n " + ds[i].chiPhi(20,5) );
		}
	}
}
