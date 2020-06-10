public class Student implements Observer<String> {
	private final String name;

	public Student( final String name ) {
		this.name = name;
	}

	@Override
	public void update( final String announcement) {
		System.out.println( "student with name: " + name + " receiving " + announcement);
	}
}