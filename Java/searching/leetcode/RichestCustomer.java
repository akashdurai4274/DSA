package searching.leetcode;

/* https://leetcode.com/problems/richest-customer-wealth/description/ */

public class RichestCustomer {
    public static void main(String[] args) {
        int[][] arr = {
                { 1, 5 },
                { 7, 3 },
                { 3, 5 }
        };
        System.out.println(find_rich(arr));
    }

    public static int find_rich(int[][] arr) {
        int maxRich = 0;
        int sum = 0;
        for (int[] i : arr) {
            for (int j : i) {
                sum += j;
            }
            maxRich = Math.max(maxRich, sum);
            sum = 0;
        }
        return maxRich;
    }
}
