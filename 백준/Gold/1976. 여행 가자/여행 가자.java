import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static ArrayList<ArrayList<Integer>> graph;
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                int connect = Integer.parseInt(st.nextToken());
                if (connect == 1) {
                    graph.get(i).add(j);
                }
            }
        }
        st = new StringTokenizer(br.readLine());

        int check = Integer.parseInt(st.nextToken());
        while (st.hasMoreTokens()) {
            int next = Integer.parseInt(st.nextToken());

            if (check == next) {
                continue;
            }

            if (!bfs(check, next)) {
                System.out.println("NO");
                return;
            }
            check = next;
        }
        System.out.println("YES");
    }

    static boolean bfs(int s, int e) {
        boolean[] check = new boolean[n+1];
        Arrays.fill(check, false);

        Queue<Integer> q = new LinkedList<>();
        q.offer(s);
        check[s] = true;

        while(!q.isEmpty()) {
            int v = q.poll();
            for (int i = 0; i < graph.get(v).size(); i++) {
                int w = graph.get(v).get(i);

                if (e == w) {
                    return true;
                }

                if (!check[w]) {
                    check[w] = true;
                    q.offer(w);
                }
            }
        }
        return false;
    }
}
