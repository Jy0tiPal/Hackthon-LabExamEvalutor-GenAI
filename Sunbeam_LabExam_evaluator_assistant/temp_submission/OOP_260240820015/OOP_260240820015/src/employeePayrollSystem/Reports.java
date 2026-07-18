package employeePayrollSystem;
import employeePayrollSystem.Program;

import java.util.Scanner;

import employeePayrollSystem.Employee;
public class Reports {

	public static Scanner sc=new Scanner(System.in);
	public static void printAllEmployees() {
		Program.emplist.forEach(emp->System.out.println(emp.toString()));
	}
	
	public static void printEmployeesByDept() {
		System.out.println("Enter dept :");
		String dept=sc.next();
		for (Employee emp : Program.emplist) {
			if(Program.emplist.equals(dept)) {
				emp.toString();
			}
		}
	}
	
}
