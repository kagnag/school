package buoi3;

import java.util.Scanner;

import buoi2.Date;

public class Gach {
	private String ms, mau;
	private	int sl, dai, ngang;
	private long gia;
	private Date ngaySx;
	private int svn, svd, sv;

	public Gach(){
		ms = new String();
		mau = new String();
		sl = dai = ngang = 0;
		gia = 0;
		ngaySx = new Date();
	}
	
	public Gach(String ms1, String mau1, int sl1, int ngang1,int dai1, long gia1, Date ngaySx1) {
		ms = ms1;
		mau = mau1;
		sl = sl1;
		ngang = ngang1;
		dai = dai1;
		gia = gia1;
		ngaySx = ngaySx1;
	}

	public Gach(Gach G) {
		ms = new String(G.ms);
		mau = new String(G.mau);
		sl = G.sl;
		dai = G.dai;
		ngang = G.ngang;
		gia = G.gia; 
		ngaySx = new Date(G.ngaySx);
	}
	
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap ma so hop gach ");
		ms = sc.nextLine();
		System.out.println("Nhap mau vien gach ");
		mau = sc.nextLine();
		System.out.println("Nhap so luong vien gach trong hop ");
		sl = sc.nextInt();
		System.out.println("Nhap chieu dai va chieu ngang vien gach ");
		dai = sc.nextInt();
		ngang = sc.nextInt();
		System.out.println("Nhap gia hop gach ");
		gia = sc.nextLong();
	/*	System.out.println("Nhap ngay san xuat ");
		ngaySx.nhap(); */
	}
	
	public void in() {
		 System.out.println("Ma so " + ms + ", mau " + mau + ", so luong " + sl+ ", chieu dai " + dai + ", chieu ngang " + ngang + ", gia " + gia + ", ngay san xuat " + ngaySx +"\n");
	}
	
	public int SoHopMin(int D, int N) {
		int svn = N / ngang;
		if(N % ngang != 0) svn++;
		int svd = D / dai;
		if(D % dai != 0) svd++;
		int sv = svn + svd;
		int SHop = sv/sl;
		if(sv % sl != 0) SHop++;
		return SHop;
	}
	 
	public long giaBanLe() {
		return (long) (gia/sl*1.2);
	}
	
	public long chiPhi(int D, int N) {
		long cp = 0;
		cp = SoHopMin(D,N)*gia + sv%sl*giaBanLe();
		return cp;	
	}
	
	public long layGia() {
		return gia;
	}
	
	public String layMS() {
		return ms;
	}
	
	public float cpThap() {
		return (float) layGia()/dtGach();
	}
	
	public long dtGach() {
		return ngang*dai;
	}
	
	public long dtHopGach() {
		return sl*ngang*dai;
	}
	
	public int minHopGach(int dai, int ngang) {
		return (int) dtHopGach()/SoHopMin(dai,ngang);
	}
	
	
}
