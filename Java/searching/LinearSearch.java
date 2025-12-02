package searching;

public class LinearSearch {
    public static void main(String[] args) {
        int[] arr = { 43, 33, 53, 4, -3, 32, 1 };

        String name = "Akash Choudri Durai";
        int target = 9;
        System.out.println(normal_search(arr, target));
        System.out.println(normal_search2(arr, target));
        System.out.println(search_with_range(arr, target, 0, 4));
        System.out.println(search_in_string(name, 'O'));
        System.out.println(search_in_string2(name, 'o'));
        System.out.println(find_minimum_number(arr));
        System.out.println(find_minimum_number2(arr));
        System.out.println(find_maximum_number(arr));
        System.out.println(find_maximum_number2(arr));

    }

    public static int normal_search(int[] arr, int target) {
        System.out.println("Normal Search:");
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    public static boolean normal_search2(int[] arr, int target) {
        System.out.println("Normal Search Boolean Variant:");
        for (int i : arr) {
            if (i == target) {
                return true;
            }
        }
        return false;
    }

    public static int search_with_range(int[] arr, int target, int start, int end) {
        System.out.println("Search With Range:");
        for (int i = start; i < end; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }

    public static int search_in_string(String name, char target) {
        System.out.println("Search In String:");
        for (int i = 0; i < name.length(); i++) {
            if (name.charAt(i) == target) {
                return i;
            }
        }
        return -1;
    }

    public static boolean search_in_string2(String name, char target) {
        System.out.println("Search In String2:");
        for (char ch : name.toCharArray()) {
            if (ch == target) {
                return true;
            }
        }
        return false;
    }

    public static int find_minimum_number(int[] arr) {
        System.out.println("Minimum Number");
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }

    public static int find_minimum_number2(int[] arr) {
        System.out.println("Minimum Number2");
        int min = Integer.MAX_VALUE;
        for (int i : arr) {
            if (i < min) {
                min = i;
            }
        }
        return min;
    }

    public static int find_maximum_number(int[] arr) {
        System.out.println("Maximum Number");
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }

    public static int find_maximum_number2(int[] arr) {
        System.out.println("Maximum Number2");
        int max = Integer.MIN_VALUE;
        for (int i : arr) {
            if (i > max) {
                max = i;
            }
        }
        return max;
    }

}
