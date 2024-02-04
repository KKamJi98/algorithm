import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			System.out.print("판별할 정수를 입력해 주세요(종료 = 0 입력) => ");
			long numInput = sc.nextLong();
			if(numInput == 0){
				break;
			}
			if (numInput % 2 == 0) {
				System.out.printf("숫자 %d는 짝수입니다.\n", numInput);
			} else {
				System.out.printf("숫자 %d는 홀수입니다.\n", numInput);
			}
		}
	}
}