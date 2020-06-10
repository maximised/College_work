public class Recursion {
	public Integer sum( Integer num ) {
		if( num == 1 ) {
			return num;
		}
		else {
			return sum(num - 1) + num;
		}
	}

	public static void main( String[] args ) {
        Integer num = 4;

        Recursion rec = new Recursion();
        Integer answer = rec.sum( num );

        System.out.println( answer );
    }
}