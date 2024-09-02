import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        int[][] arr = new int[T][2];

        String[] sp;
        for (int i = 0; i < T; i++) {
            sp = br.readLine().split(" ");
            arr[i][0] = Integer.parseInt(sp[0]);
            arr[i][1] = Integer.parseInt(sp[1]);
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < T; i++) {
            int rank = 1;

            for (int j = 0; j < T; j++) {
                if (i == j) continue;
                if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) {
                    rank++;
                }
            }
            sb.append(rank).append(' ');
        }
        System.out.println(sb);
    }
}