import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static long max = 10000000000L;
    static int n, left, right;
    static long l, r;
    static long[] array;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        array = new long[n];
        for (int i = 0; i < n; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(array);
        //System.out.println(Arrays.toString(array));

        left = 0;
        right = n-1;
        while (left < right) {
            long temp = array[left] + array[right];

            if (Math.abs(temp) <= max) {
                max = Math.abs(temp);
                l = array[left];
                r = array[right];
            }

            if (temp <= 0) {
                left++;
            } else {
                right--;
            }
        }

        System.out.println(l + " " + r);
    }
}