import javax.swing.plaf.IconUIResource;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);

        int left = 0;
        int right = 0;
        int resultNum = 2_100_000_000;
        while (left<n) {
            if (Math.abs(arr[left] - arr[right]) < m) {
                left++;
                continue;
            }
            if (Math.abs(arr[left] - arr[right]) == m) {
                resultNum = m;
                break;
            }
            resultNum = Math.min(resultNum, Math.abs(arr[left] - arr[right]));
            right++;

        }

        System.out.println(resultNum);
    }
}
