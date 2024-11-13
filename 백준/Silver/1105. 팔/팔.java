import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int ans = 0;
        String L = st.nextToken();
        String R = st.nextToken();

        if (L.length() != R.length())
            System.out.println(ans);
        else {
            int i = 0;
            while (i < L.length() && L.charAt(i) == R.charAt(i)) {
                if (L.charAt(i) == '8') {
                    ans++;
                }
                i++;
            }
            System.out.println(ans);
        }
    }
}