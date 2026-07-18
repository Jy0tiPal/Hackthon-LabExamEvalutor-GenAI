package employeePayrollSystem;

public class Employee {

	private int empid;
	private String name;
	private double salary;
	private String deparement;
	private boolean transactions=true;
	
	public Employee(int empid, String name, double salary, String deparement) {
		this.empid = empid;
		this.name = name;
		this.salary = salary;
		this.deparement = deparement;
	}

	public Employee() {
		// TODO Auto-generated constructor stub
	}

	public int getEmpid() {
		return empid;
	}

	public void setEmpid(int empid) {
		this.empid = empid;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getSalary() {
		return salary;
	}

	public void setSalary(double salary) {
		this.salary = salary;
	}

	public String getDeparement() {
		return deparement;
	}

	public void setDeparement(String deparement) {
		this.deparement = deparement;
	}

	public boolean getTransactions() {
		return transactions;
	}

	public void setTransactions(boolean transactions) {
		this.transactions = transactions;
	}
	
	
	
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return String.format("%-10d %-15s %-10lf %-10s %-10lf",empid,name,salary,deparement,transactions);
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + empid;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if(obj==null)
			return false;
		if (!(obj instanceof Employee))
			return false;
		Employee other = (Employee) obj;
		if(empid==other.empid||deparement==other.deparement)
			return true;
		return false;
	}
}
