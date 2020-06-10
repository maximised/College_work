import java.util.*;

public class Compare<T> implements Comparable<Compare> {
	public T attribute;

	public Compare(T attr) {
		this.attribute = attr;
	}

	@Override
	public int compareTo(T o) {
		return (this.attribute < o.attribute ? -1 : this.attribute > o.attribute ? 1 : 0);
	}
}