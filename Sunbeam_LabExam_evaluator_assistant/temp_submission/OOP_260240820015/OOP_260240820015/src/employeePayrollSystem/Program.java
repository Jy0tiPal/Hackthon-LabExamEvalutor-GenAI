package employeePayrollSystem;
import employeePayrollSystem.Employee;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Program {
	public static Scanner sc=new Scanner(System.in);
	public static List<Employee>emplist=new ArrayList<>();
	
	public static int menuList() {
		System.out.println("0.exit");
		System.out.println("1.Add employee");
		System.out.println("2.Add Bonous");
		System.out.println("3.Deduct salary");
		System.out.println("4.print All Employees");
		System.out.println("5.display by dept");
		System.out.println("Top k employees");
		
		System.out.println("Enter you choice :");
		int choice=sc.nextInt();
		return choice;
	}
	public static void acceptRecord(int []empid) {
		System.out.println("Enter empid:");
		empid[0]=sc.nextInt();
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int []empid=new int[1];
		int choice;
		while((choice=menuList())!=1) {
			try {
				switch(choice) {
				case 1:
					acceptRecord(empid);
					EmployeeManagement.addEmployee(empid[0]);
					break;
				case 2:
					
					break;
				case 3:
					
					break;
				case 4:
					Reports.printAllEmployees();
					break;
				case 5:
					Reports.printEmployeesByDept();
					break;
					
				case 6:
					topkEmployees();
					break;
					
				}
			}
			catch(Custom_exception e) {
				e.getMsg();
			}
		}

	}

}
