package Maths;

import java.util.Scanner;

public class CharacterFrequency {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        frequency_check(input);
    }

    public static void frequency_check(Scanner input) {
        String str = input.nextLine();
        str = str.toUpperCase();

        int[] arr = new int[26];
        for (int i = 0; i < str.length(); i++) {
            arr[str.charAt(i) - 'A']++;
        }

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 0) {
                char ch = (char) (i + 'A');
                System.out.println(ch + "-" + arr[i]);
            }
        }
    }
}
