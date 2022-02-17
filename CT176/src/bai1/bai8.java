package bai1;
import java.util.Scanner;

import buoi2.Diem;

public class bai8{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n, x;
		int[] arr = new int[100];
		System.out.println("Nhap so phan tu cua mang ");
		n = sc.nextInt();
		for(int i=0; i<n; i++) {
			System.out.println("Nhap phan tu thu " + (i+1));
			arr[i] = sc.nextInt();
		}
		System.out.println("Mang gom cac phan tu "); 
		for(int i=0; i<n; i++) {
			System.out.print(" " + arr[i]);}

		System.out.println("\nNhap vao so nguyen x bat ky ");
		x = sc.nextInt();
		int count = 0;
		for(int i=0; i<n; i++) {
			if(arr[i]==x) count ++;		
		}
		System.out.println("Danh sach co "+ count + " phan tu so " + x);

		System.out.println("Sap xep mang tang dan ");
		int temp;
		for(int i=0; i<n-1; i++) {
			for(int j=i+1; j<n; j++) {
				if(arr[i]>arr[j]) {
					temp = arr[i];	
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
		}	
		System.out.println("Mang sao khi sap xep la");
		for(int i=0; i<n; i++) {
			System.out.print(" " + arr[i]);
			}

	}
}