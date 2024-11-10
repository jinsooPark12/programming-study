import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    static int[] parent, level;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int F = Integer.parseInt(br.readLine());

            parent = new int[F*2];
            level = new int[F*2];
            for (int j = 0; j < F*2; j++) {
                parent[j] = j;
                level[j] = 1;
            }

            int idx = 0;
            Map<String, Integer> m = new HashMap<>();
            for (int j = 0; j < F; j++) {
                st = new StringTokenizer(br.readLine());
                String a = st.nextToken();
                String b = st.nextToken();

                if (!m.containsKey(a)) {
                    m.put(a, idx++);
                }
                if (!m.containsKey(b)) {
                    m.put(b, idx++);
                }

                sb.append(union(m.get(a), m.get(b)) + "\n");
            }
        }
        System.out.println(sb.toString());
    }

    public static int find(int x) {
        if (x == parent[x]) return x;

        return parent[x] = find(parent[x]);
    }

    public static int union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x != y) {
            parent[y] = x;
            level[x] += level[y];
        }

        return level[x];
    }
}
