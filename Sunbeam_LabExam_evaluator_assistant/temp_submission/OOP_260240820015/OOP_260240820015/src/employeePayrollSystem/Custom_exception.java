package employeePayrollSystem;

public class Custom_exception extends Exception {

	String msg;
	public Custom_exception() {
		// TODO Auto-generated constructor stub
	}
	public Custom_exception(String msg) {
		this.msg = msg;
	}
	
	public void getMsg() {
		// TODO Auto-generated method stub
		System.out.println(msg);
	}
	
}
