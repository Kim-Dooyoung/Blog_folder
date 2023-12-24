public class _02_Ch2 {
    public static void main(String[] args) {
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
        
    }

}
