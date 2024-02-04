// 다음의 맵 grade에서 "B'에 해당되는 값을 추출해 보자. (추출하고 나면 grade에는 "B"에 해당하는 아이템이 사라져야 한다.)
import java.util.HashMap;

public class Main {
	public static void main(String[] args) {
		HashMap<String, Integer> grade = new HashMap<>();
		grade.put("A", 90);
		grade.put("B", 80);
		grade.put("C", 70);

//		System.out.println(grade.get("B"));
		System.out.println(grade.remove("B"));
		System.out.println(grade);
	}
}