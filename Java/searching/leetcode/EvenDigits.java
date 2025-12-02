package searching.leetcode;

/* https://leetcode.com/problems/find-numbers-with-even-number-of-digits/ */

public class EvenDigits {
    public static void main(String[] args) {
        int[] num = { 234, 4334, 12, 4343, 455, 6543 };
        System.out.println(findDigits(num));
    }

    public static int findDigits(int[] num) {
        int count = 0;
        for (int i = 0; i < num.length; i++) {
            if (even(num[i])) {
                count++;
            }
        }
        return count;
    }

    public static boolean even(int num) {
        return digit(num) % 2 == 0;
    }

    public static int digit(int num) {
        int count = 0;
        while (num > 0) {
            count++;
            num = num / 10;
        }
        return count;
    }

    public static int digit2(int num) {
        return (int) Math.log10(num) + 1;
    }
}
