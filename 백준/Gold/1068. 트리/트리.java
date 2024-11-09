import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static ArrayList<Integer>[] graph;
    static int ans, point, s;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int parent = Integer.parseInt(st.nextToken());

            if (parent == -1) {
                s = i;
                continue;
            }

            graph[parent].add(i);
        }
        point = Integer.parseInt(br.readLine());
        dfs(s);
        System.out.println(ans);
    }

    public static void dfs(int start) {
        if (start == point) return;
        if (graph[start].isEmpty()) {
            ans++;
            return;
        }
        if (graph[start].size() == 1 && graph[start].get(0) == point){
            ans++;
            return;
        }

        for (int next : graph[start]) {
            dfs(next);
        }
    }
}
