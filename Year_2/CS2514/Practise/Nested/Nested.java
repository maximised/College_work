public class Nested {
	public static void main( String[] args ) {

		print_number( 21 );

	}

	public static void print_number( Integer n ) {
		Integer num = n;

		class Print {
			public void print_num() {
				System.out.println( num );
			}
		}

		Print p = new Print();

		p.print_num();
	} 
}