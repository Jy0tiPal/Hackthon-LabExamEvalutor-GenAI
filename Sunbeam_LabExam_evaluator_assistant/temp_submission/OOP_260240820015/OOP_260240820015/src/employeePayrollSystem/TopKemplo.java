package employeePayrollSystem;

import java.util.Scanner;
public class TopKemplo {

	public static void topkEmployees() {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the top k(limit):");
		int k=sc.nextInt();
		System.out.println("Enter the minmum salary:");
		double sal=sc.nextDouble();
		Program.emplist.sort((x,y)->-Double.compare(x.getSalary(), y.getSalary()));
		for(int i=Program.emplist.size();i>=k;i--) {
			Employee emp=Program.emplist.get(i);
			System.out.println(emp.toString());
		}
	}
}
