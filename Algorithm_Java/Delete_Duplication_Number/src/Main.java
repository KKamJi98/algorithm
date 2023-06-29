// 다음의 numbers 리스트에서 중복 숫자를 제거해 보자.
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) {
		ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5));
		System.out.println(numbers);


		HashSet<Integer> numbers2;

// 방법 1
//		for(Integer ele : numbers){
//			numbers2.add(ele);
//		}

// 방법 2
//		numbers2.addAll(numbers);

// 방법 3
		numbers2 = new HashSet<>(numbers);

		System.out.println(numbers2);
	}
}