import java.util.*;

public class Teacher implements Subject<String, String> {
	private final String name;
	private final List<Observer<String>> students;

	public Teacher( final String name ) {
		this.name = name;
		this.students = new ArrayList<Observer<String>>();
	}

    @Override
	public void attach( final Observer<String> student ) {
		students.add( student );
		System.out.println( "student with name: " + student + " added!" );
	}

	@Override
	public void detach( final Observer<String> student ) {
		students.remove( student );
		System.out.println( "student with name: " + student + " removed!" );
	}

	@Override
	public void notify( final String announcement ) {
		System.out.println( "teacher with name " + name + " making announcement!" );
		for (Observer student: students) {
			student.update( announcement );
		}
	}
}