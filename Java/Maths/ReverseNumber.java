package Maths;

public class ReverseNumber {
    public static void main(String[] args) {
        System.out.println(reverse_number(123456));
    }

    public static int reverse_number(int number) {
        int result = 0;
        while (number > 0) {
            result = result * 10 + (number % 10);
            number = number / 10;
        }
        return result;
    }
}
