package employeePayrollSystem;
import java.util.Scanner;
import employeePayrollSystem.Program;
import employeePayrollSystem.Custom_exception;
public class EmployeeManagement {

	public static void addEmployee(int empid){
		Scanner sc=new Scanner(System.in);
		Employee key=new Employee();
		key.setEmpid(empid);
		try {
			if(!(Program.emplist.contains(key))) {
				System.out.println("Enter name:");
				String name=sc.next();
				System.out.println("Enter salary:");
				double sal=sc.nextDouble();
				System.out.println("Enter depart:");
				String dept=sc.next();
				Program.emplist.add(new Employee(empid,name,sal,dept));
			}else {
				throw new Custom_exception("Empid already exists");
			}
		}
		catch(Custom_exception e) {
			e.getMsg();
		}
	}

}
