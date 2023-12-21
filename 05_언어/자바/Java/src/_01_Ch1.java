import com.sun.xml.internal.ws.api.model.wsdl.WSDLOutput;

public class _01_Ch1 {
    // o 자바언어의 특징
    // 1. 운영체제에 독립적 -> 자바가상머신(JVM)을 사용해서 가능
    // 2. 객체지향언어
    // 3. 비교적 배우기 쉬움
    // 4. 자동 메모리 관리 -> 가비지걸렉터(garbage collector)가 자동적으로 메모리를 관리
    // 5. 내트워크와 분산처리를 지원 -> Java API를 통해 네트워크 관련 프로그램을 쉽게 개발할 수 있도록 지원
    // 6. 멀리쓰레드 지원
    // 7. 동적 로딩 지원

    // o JVM(Java Virtual Machine)
    // JVM : 자바를 실행하기 위한 가상 컴퓨터
    // 애플리케이션과 OS사이에 JVM이 있어 이를 거치고 전달

    // Hello.java로 가정하고
    // Hello.java 작성 -(javac.exe 컴파일)> Hello.class 생성 -(java.exe 실행)> "Hello, world." 출력
    public static void main(String[] args) {
        System.out.println("Hello, world."); // 화면에 글자를 출력
    }

    // 모든 코드는 클래스 안에 존재하여야 함
    // class 클래스 이름 {
    // public static void main(String[] args) { // main메서드의 선언부 / 반드시 하나를 가지고 있어야 함
    /*
           주석을 제외한 모든 코드는 클래스의 블럭 {} 내에 작성해야 함
           실행될 문장들을 적는다
    */
    // }
    // }

    // 자주 발생하는 에러와 해결방법
    // 종류는 책 참조
    // 에러 메시지를 읽고 해당 부분과 그 주위 코드를 살펴본다 -> 이상없으면 기본적인 부분 재확인 -> 의심가는 부분을 주석처리 혹은 따로 때어내어 테스트

    // 자바프로그램 실행과정
    // 클래스(*.class파일) 로드 -> 클래스파일 검사 -> 클래스에서 main호출

    // 주석
    // 범위 주석 : /* ~~ */
    // 한 줄 주석 : //
}