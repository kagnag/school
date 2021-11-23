package bai1;

import java.util.Scanner;

public class Ptb2 {	
	static Scanner sc = new Scanner(System.in);
	public static void bacnhat(float b,float c) {
		float s=0;
		if(b==0) {
			System.out.println("Phuong trinh vo nghiem");
		}
		s =(float) -c/b;
			System.out.println("Nghiem cua pt bang x= " +s);
	}
	public static void bachai(float a,float b,float c) {
		if (a==0){
			bacnhat(b,c);
			return ;
		} else{
			float delta;
			float x, x1, x2;
			delta = (float) b*b - 4*a*c;
			if(delta<0) {
				System.out.println("Phuong trinh vo nghiem");
			} else if (delta==0){
				x= -b/(2*a);
				System.out.println("Phuong trinh co nghiem kep x1 = x2 = "+x);
			} else if(delta>0){
				x1 = (float) ((-b-Math.sqrt(delta))/(2*a));
				x2 = (float) ((-b+Math.sqrt(delta))/(2*a));
				System.out.println("PT co 2 nghiem phan biet x1 = "+x1+", x2 = "+x2);
			}
		}
	}
	public static void main(String[] args) {
		float a, b, c;
		System.out.println("Nhap a:");
		a = sc.nextFloat();
		System.out.println("Nhap b:");
		b = sc.nextFloat();
		System.out.println("Nhap c:");
		c = sc.nextFloat();
		bachai(a,b,c);
	}
}