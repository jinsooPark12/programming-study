import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] st = br.readLine().split(" ");

        long[] arr = new long[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(st[i]);
        }
        Arrays.sort(arr);
        int count = 0;

        for (int i = 0; i < N; i++) {
            int start = 0;
            int end = N-1;
            long k = arr[i];
            while (start < end) {
                long sum = arr[start] + arr[end];
                if (sum == k) {
                    if (i == start) {
                        start++;
                    } else if (i == end) {
                        end--;
                    } else {
                        count++;
                        break;
                    }
                } else if (sum > k) {
                    end--;
                } else {
                    start++;
                }
            }
        }
        System.out.println(count);
    }
}