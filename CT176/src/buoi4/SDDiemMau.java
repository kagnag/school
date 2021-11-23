package buoi4;

public class SDDiemMau {

	public static void main(String[] args) {
		DiemMau A = new DiemMau(5,10,"Trang");
		A.in();
		DiemMau B = new DiemMau();
		B.nhap();
		B.in();
		System.out.println("Doi diem B mot toa do(5,3) ");
		B.doiDiem(10,8);
		B.ganMau("Vang");
		B.in();	
	}

}
