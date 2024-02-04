// 주민등록번호를 년, 월, 일 부분과 그 뒤의 숫자 부분으로 나누어 출력
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String identificationNumberInput;
		identificationNumberInput = sc.next();

		String year = identificationNumberInput.substring(0, 2);
		String month = identificationNumberInput.substring(2, 4);
		String day = identificationNumberInput.substring(4, 6);
		String others = identificationNumberInput.substring(7);

		System.out.println("년 => " + year);
		System.out.println("월 => " + month);
		System.out.println("일 => " + day);
		System.out.println("뒷자리 => " + others);
	}
}