package searching;

import java.util.Arrays;

public class LinearSearchII {
    public static void main(String[] args) {
        int[][] matrix = { { 1, 2, 3 }, { 4, 5 }, { 7, 8, 9 } };
        int target = 4;
        System.out.println(Arrays.toString(search_in_2dArray(matrix, target)));
        System.out.println(search_in_2dArray2(matrix, target));
    }

    public static int[] search_in_2dArray(int[][] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if (arr[i][j] == target) {
                    return new int[] { i, j };
                }
            }
        }
        return new int[] { -1, -1 };
    }

    public static boolean search_in_2dArray2(int[][] arr, int target) {
        for (int[] i : arr) {
            for (int j : i) {
                if (j == target) {
                    return true;
                }
            }
        }
        return false;
    }
}
