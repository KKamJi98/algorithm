// A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

public class Main {
	public static void main(String[] args) {
		int[] marks = {70, 60, 55, 75, 95, 90, 80, 80, 85, 95};

		double avgScore = 0;

		for (int element : marks){
			avgScore += element;
		}
		System.out.println("A 학급의 평균 점수는 " + avgScore / marks.length + "점 입니다");
	}
}