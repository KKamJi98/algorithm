import org.w3c.dom.ls.LSOutput;

class Student{
	String name;
	Integer koreanScore;
	Integer englishScore;
	Integer mathScore;
	Student(String nameIn, Integer koreanScoreIn, Integer englishScoreIn, Integer mathScoreIn){
		this.name = nameIn;
		this.koreanScore = koreanScoreIn;
		this.englishScore = englishScoreIn;
		this.mathScore = mathScoreIn;
	}
	Double getAverage(){
		return ((double)(koreanScore + englishScore + mathScore))/3.0;
	}

	void getInfo(){
		System.out.printf("이름 => %s\n국어점수 => %d \n영어점수 => %d \n수학점수 => %d \n평균 => %.2f", this.name, this.koreanScore, this.englishScore, this.mathScore, getAverage());
	}
}

public class Main {
	public static void main(String[] args) {
		Student student1 = new Student("홍길동", 85, 72, 55);
		student1.getInfo();

	}
}