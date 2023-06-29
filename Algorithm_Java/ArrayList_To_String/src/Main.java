// 다음과 같은 ['Life', 'is', 'too', 'short'] 리스트를 "Life is too short" 문자열로 만들어 출력해 보자.
import java.util.ArrayList;
import java.util.Arrays;


public class Main {
	public static void main(String[] args) {
		ArrayList<String> myList = new ArrayList<>(Arrays.asList("Life", "is", "too", "short"));
		System.out.println(myList);

		String myString;
		myString = String.join(" ", myList);
		System.out.println(myString);
	}
}