import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[][] matrix = new int[n+1][n+1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        long dp[][] = new long[n+1][n+1];
        dp[1][1] = 1;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                int next = matrix[i][j];
                if (next == 0) break;
                if (j+next<=n) dp[i][j+next] += dp[i][j];
                if (i+next<=n) dp[i+next][j] += dp[i][j];
            }
        }
        System.out.println(dp[n][n]);
    }
}
