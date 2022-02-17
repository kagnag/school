package buoi4;
import java.util.Scanner;
public class SDConVat {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		ConVat cv;
		ConVat ds[];
		System.out.println("Nhap so con vat: ");
		int n;
		n = sc.nextInt();
		sc.nextLine();
		ds = new ConVat[n];
		char c = ' ';
		for(int i=0; i<n; i++) {
			boolean tr = false;
			do{
				System.out.println("Nhap con Bo(b), con de(d), con Heo(h).");
				c = sc.nextLine().charAt(0);
				if(c != 'b' && c != 'd' && c!= 'h') {
					System.out.print("Ban nhap khong hop le... \nNhap lai: ");
					tr = true;
				}
				else break;
			} while (tr == true);

			if(c == 'b') ds[i] = new Bo();
			else if(c == 'd') ds[i] = new De();
			else if(c == 'h') ds[i] = new Heo();
			else continue;
			ds[i].nhap();
		}

		for(int i=0; i<n; i++) {
			ds[i].in();
			ds[i].Keu();
		}

	}

}
