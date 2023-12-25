public class _02_Ch2 {
    public static void main(String[] args) {
        // 1. 변수
        // 변수 : 단 하나의 값을 저장할 수 있는 메모리 공간
        // 변수 선언
        // int age; // age라는 이름의 변수를 선언 / int는 변수 타입, age는 변수 이름
        // 변수의 초기화 : 변수를 사용하기 전에 처음으로 값을 저장하는 것
        // int age = 25; // 변수 age를 선언하고 25로 초기화한다.
        /* int a, b;
        int x = 0, y = 0;
         위와 같은 방식도 사용 가능*/

        // 2-1
        int year = 0;
        int age = 14;

        System.out.println(year);
        System.out.println(age);

        year = age + 2000;
        age = age + 1;

        System.out.println(year);
        System.out.println(age);

        // 두 변수의 값 교환하기
        // 변수를 하나 더 생성해서 임시 저장소로 사용

        // 2-2
        int x = 10, y = 20;
        int tmp = 0;

        System.out.println("x:"+ x + " y:" + y);

        tmp = x;
        x = y;
        y = tmp;

        System.out.println("x:"+ x + " y:" + y);

        // 변수의 명명규칙
        // 식별자 : 프로그래밍에서 사용하는 모든 이름
        // 식별자를 생성할 때의 규칙
        // 1. 대소문자가 구분되며 길이에 제한이 없다.
        // 2. 예약어를 사용해서는 안된다.
        // 3. 숫자로 시작해서는 안된다.
        // 4. 특수문자는 '_'와 '$'만을 허용한다.
        // 권장 규칙
        // 1. 클래스 이름의 첫 글자는 항상 대문자로 한다.
        // 2. 여러 단어로 이루어진 이름은 단어의 첫 글자르 대문자로 한다.
        // 3. 상수의 이름은 모두 대문자로 한다. 여러 단어로 이루어진 경우 '_'로 구분한다.

        // 2. 변수의 타입
        // 자료형 : 값의 종류에 따라 값이 저장될 공간의 크기와 저장형식을 정의한 것
        // 문자형(char), 정수형(byte, short, int long), 실수형(float, double) 등
        // 기본형 : 실제 값을 저장 / 참조형 : 객체의 주소를 저장
        
    }

}
