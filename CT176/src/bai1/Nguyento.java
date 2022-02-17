package bai1;
import java.util.Scanner;

	public class Nguyento {
	static Scanner sc = new Scanner(System.in);
	
	public static void check(int a) {
		int i=2;
		int x=0;
	while(i<Math.sqrt(a) && x==0) {
		if(a%i==0) x=1;
		i++;
	}
		if(x==0)
			System.out.println("so da nhap la so nguyen to. ");
		else System.out.println("so da nhap ko la so nguyen to. ");
	}
	
	public static void nhiphan(int a) {
		String x ="";
				while(a!=0){
			x+=a%2+ ",";
			a/=2;
		}
		String []y=x.split(",");
		String b="";
		for(int i=0; i<y.length;i++)
			b+=y[y.length-i-1];
			
		System.out.println(" b = "+b);	
		
	}
	public static void main(String[] args) {
		System.out.println("Nhap mot so: ");
		int a = sc.nextInt();
		check(a);
		nhiphan(a);
		// String s = Integer.toBinaryString(n); S.o.p(s)
	}
	}
