package Java.Strings;

public class index {
    public static void main(String[] args) {
        String a = "hello";
        String b = "Hello";

        System.out.println(a == b); // true (same pool reference)
        System.out.println(a.equals(b)); // true (same content)
    }
}
