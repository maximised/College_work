public class Exceptions {
	private int i = 0;
	public void foo() throws Exception {
		if ( i == 0 ) {
			throw new Exception();
		}
		else {
			System.out.println( "we're okay!" );
		}
	}

	public void test_foo() {
		try {
			System.out.println( "testing" );
			this.foo();
		}
		catch ( Exception ex ) {
			System.out.println( "error happened" );
		}
		finally {
			System.out.println( "end testing");
			System.out.println();
		}
	}

	public void append_i() {
		i++;
	}

	public static void main( String[] args ) {
		Exceptions e1 = new Exceptions();
		e1.append_i();
		e1.test_foo();

		Exceptions e2 = new Exceptions();
		e2.test_foo();
	}
}