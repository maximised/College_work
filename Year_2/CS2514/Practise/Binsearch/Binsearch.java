import java.util.*;

public class Binsearch {
	public static int Binsearch( Comparable item, Comparable[] items, int lo, int hi ) {
		final int result;
		if (lo > hi) {
			result = - 1;
		} else {
			int mid = (lo + hi) / 2;
			int outcomeOfComparison = item.compareTo( items[ mid ] );
			if (outcomeOfComparison == 0) {
				result = mid;
			} else if (outcomeOfComparison < 0) {
				result = Binsearch( item, items, lo, mid - 1 );
			} else {
				result = Binsearch( item, items, mid + 1, hi );
			}
		}
		return result;
	}

	public static void main( String[] args ) {
        Integer[] nums =  new Integer[]{1,1,3,4,5,6};

        Arrays.sort(nums);
        Integer lo = 0;
        Integer hi = nums.length-1;

        Integer pos = Binsearch.Binsearch( 1, nums, lo, hi );

        System.out.println(pos);
    }
}

