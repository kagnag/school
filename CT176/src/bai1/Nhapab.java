package bai1;
import java.util.Scanner;
public class Nhapab{
	static Scanner sc = new Scanner(System.in);
	public static int nhap() {	
		int n;
		int a = 0;
		n = Integer.MAX_VALUE;
		String s;
		System.out.println("Nhap mot so: ");
			while(n == Integer.MAX_VALUE) {

			s = sc.nextLine();
			try {
				a = Integer.parseInt(s);
				n = 1;
			}
				catch(NumberFormatException e){ 
					 n = Integer.MAX_VALUE;
					 System.out.println("Sai dinh dang so, nhap lai: ");
				 }	
		}
		return a;
	}
	public static void main(String[] args) {
		
			int a = nhap();
			int b = nhap();
		System.out.println(a +"+" + b +"=" +(a+b));
}
}
	


