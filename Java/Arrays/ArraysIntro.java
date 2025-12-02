package Arrays;

import java.util.Arrays;
import java.util.Scanner;

public class ArraysIntro {

    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        int[] arr = new int[5];
        int[] arr2 = { 1, 2, 3, 4, 5 };
        int[][] arr3 = new int[3][3];
        String[] arr4 = new String[2];
        int[][] sample = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        arr[0] = 1;
        arr[1] = 2;
        arr[2] = 3;
        arr[3] = 4;
        arr[4] = 5;

        /*
         * System.out.println(Arrays.deepToString(sample));
         * 
         * inputArray(arr, inp);
         * 
         * System.out.println(Arrays.toString(arr));
         */

        input2DArray(arr3, inp);

        System.out.println(Arrays.deepToString(arr3));

        /*
         * inputArrayString(arr4, inp);
         * 
         * System.out.println(Arrays.toString(arr4));
         */
        System.out.println("Print Using Enhanced For loop");

        for (int[] num : arr3) {
            // System.out.println(Arrays.toString(num));
            for (int n : num) {
                System.out.print(n + " ");
            }
            System.out.println();
        }

        inp.close();
        /*
         * for (int i = 0; i < arr.length; i++) {
         * System.out.println(arr[i]);
         * }
         */
    }

    static void inputArray(int[] arr, Scanner inp) {

        for (int index = 0; index < arr.length; index++) {
            System.out.println("Array1 Enter the Element for index " + index + ":");
            arr[index] = inp.nextInt();
        }

    }

    static void inputArrayString(String[] arr, Scanner inp) {
        for (int index = 0; index < arr.length; index++) {
            System.out.println("Enter the Element for index " + index + ":");
            arr[index] = inp.next();
        }

    }

    static void input2DArray(int[][] arr, Scanner inp) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                String message = String.format("Enter the Element for index: [%d %d]", i, j);
                // System.out.println(message);
                arr[i][j] = inp.nextInt();
            }

        }
    }

}
