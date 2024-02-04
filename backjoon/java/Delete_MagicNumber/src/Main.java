// 다음은 커피의 종류(1: 아메리카노, 2:아이스 아메리카노, 3:카페라떼)를 입력하면 커피의 가격을 알려주는 프로그램이다.
// 아래의 코드에서 1, 2, 3과 같은 매직넘버를 제거하여 프로그램을 개선해보자.

import java.util.HashMap;

public class Main {
	enum Coffee{
		AMERICANO,
		ICE_AMERICANO,
		CAFFE_LATTE
	}
	static void printCoffeePrice(Coffee type) {
		HashMap<Coffee, Integer> priceMap = new HashMap<>();
		priceMap.put(Coffee.AMERICANO, 3000);  // 1: 아메리카노
		priceMap.put(Coffee.ICE_AMERICANO, 4000);  // 2: 아이스 아메리카노
		priceMap.put(Coffee.CAFFE_LATTE, 5000);  // 3: 카페라떼
		int price = priceMap.get(type);
		System.out.printf("%s 가격은 %d원 입니다.%n", type, price);
	}

	public static void main(String[] args) {
		printCoffeePrice(Coffee.AMERICANO);  // "가격은 3000원 입니다." 출력
		printCoffeePrice(Coffee.CAFFE_LATTE);  // NullPointerException 발생
	}
}