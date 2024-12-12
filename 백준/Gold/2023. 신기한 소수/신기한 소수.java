import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        getResult(0, n);
        System.out.println(sb);
    }

    public static void getResult(int o, int n) {
        if (n==0) {
            if (isPrime(o)) sb.append(o).append("\n");
            return;
        }
        for (int i = 0; i < 10; i++) {
            int next = o * 10 + i;
            if (isPrime(next)) getResult(next, n-1);
        }
    }

    public static boolean isPrime(int num) {
        if (num < 2) return false;

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
