package searching;

import java.util.Arrays;

public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = { -5, -4, -3, 6, 7, 8, 9, 10, 43, 54, 65 };
        int target = -4;
        System.out.println(binary_search(arr, target));
        // System.out.println(Arrays.toString(reverse(arr)));
        System.out.println(order_agnostic_binary_search(reverse(arr), target));
    }

    public static int binary_search(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (target > arr[mid]) {
                start = mid + 1;
            } else if (target < arr[mid]) {
                end = mid;
            } else {
                return mid;
            }
        }
        return -1;
    }

    public static int order_agnostic_binary_search(int[] arr, int target) {
        System.out.println(Arrays.toString(arr));
        int start = 0;
        int end = arr.length - 1;

        while (start <= end) {
            boolean isAsc = arr[start] < arr[end];
            int mid = start + (end - start) / 2;

            if (arr[mid] == target) {
                return mid;
            }

            if (isAsc) {
                if (target > arr[mid]) {
                    start = mid + 1;
                } else if (target < arr[mid]) {
                    end = mid;
                }
            } else {
                if (target < arr[mid]) {
                    start = mid + 1;
                } else if (target > arr[mid]) {
                    end = mid;
                }
            }
        }
        return -1;

    }

    public static int[] reverse(int[] arr) {
        for (int i = 0; i < arr.length / 2; i++) {
            int temp = arr[i];
            arr[i] = arr[arr.length - 1 - i];
            arr[arr.length - 1 - i] = temp;
        }
        return arr;
    }
}
