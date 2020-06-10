public class Main {
	public static void main( String[] args ) {
		Student s1 = new Student("Philip");
		Student s2 = new Student("Michelle");

        Teacher t1 = new Teacher("George");

        t1.attach(s1);
        t1.attach(s2);

        t1.notify("extra homework Saturday");
        t1.notify("School closed next month");
	}
}