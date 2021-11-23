package buoi2;

import java.util.Scanner;

public class Diem {
	private int x, y;

	public Diem() {
		x = 0;
		y = 0;
	}

	public Diem(int x1, int y1) {
		x = x1;
		y = y1;
	}
	
	public Diem(Diem d) {
		x = d.x;
		y = d.y;
	}

	public String toString() {
		return "(" + x + "," + y + ")";
	}
	
	public void nhapDiem() {
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhap hoanh do va tung do: ");
			x = sc.nextInt();
			y = sc.nextInt();
	}

	public void hienThi() {
		System.out.print("(" + x + "," + y + ")");
	}
	
	public void doiDiem(int dx, int dy) {
		x += dx;
		y += dy;
	}
	
	public int giaTriX() {
		return x;
	}
	
	public int giaTriY() {
		 return y;		
	}
	
	public float khoangCach() {
		return (float) (Math.sqrt(Math.pow(x,2) + Math.pow(y,2)));
	}
	
	public float khoangCach(Diem d) {
		return (float) ( Math.sqrt(Math.pow(x - d.x, 2) + Math.pow(y - d.y, 2)));
	}
	
	
}
