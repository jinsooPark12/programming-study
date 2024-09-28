import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int n, m, start, end;
    static int s, e;
    static int[] visited;
    static List<Integer>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        graph = new LinkedList[n+1];
        for (int i = 0; i < n + 1; i++) {
            graph[i] = new LinkedList<>();
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            e = Integer.parseInt(st.nextToken());

            graph[s].add(e);
            graph[e].add(s);
        }
        //System.out.println(Arrays.toString(graph));
        visited = new int[n+1];

        System.out.println(dfs(start));
    }

    public static int dfs(int x) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(x);

        while (!q.isEmpty()) {
            int temp = q.poll();

            for (int next : graph[temp]) {
                if (visited[next] == 0) {
                    visited[next] = visited[temp]+1;
                    if (next == end) {
                        return visited[next];
                    }
                    q.offer(next);
                }
            }
        }
        return -1;
    }
}