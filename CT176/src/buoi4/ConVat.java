package buoi4;
import java.util.Scanner;
public abstract class ConVat {
	private String giong;
	private String maulong;
	private float cnang;
	public ConVat() {
		giong = new String();
		maulong = new String();
		cnang = 0;
	}
	public ConVat(ConVat c) {
		giong = new String(c.giong);
		maulong = new String(c.maulong);
		cnang = c.cnang;
	}
	public void nhap() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap giong cua con vat: ");
		giong = sc.nextLine();
		System.out.println("Nhap mau long cua con vat: ");
		maulong = sc.nextLine();
		System.out.println("Nhap can nang cua con vat: ");
		cnang = sc.nextFloat();
	}
	public void in() {
		System.out.println("Giong " + giong + ", mau long " + maulong + ", can nang " + cnang);
	}
	public abstract void Keu();
}
