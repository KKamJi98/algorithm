// 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력하기.

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String pin = sc.next();

		int keyIndex = pin.indexOf("-") + 1;


		if ('1' == pin.charAt(keyIndex)) {
			System.out.println("이 사람은 남자입니다");
		} else {
			System.out.println("이 사람은 여자입니다");
		}
	}

}