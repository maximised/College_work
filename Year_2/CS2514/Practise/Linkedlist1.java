import java.util.*;

public class Linkedlist1 {
	public static void main(String args[]) {
		LinkedList<String> al = new LinkedList<String>();

		al.add("fred");

		Iterator<String> itr = al.iterator();

		while (itr.hasNext()) {
			System.out.println(itr.next());
		}
	}
}