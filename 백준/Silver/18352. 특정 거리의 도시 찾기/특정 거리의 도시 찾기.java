import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, m, k, x, result;
    static ArrayList<Integer>[] graph;
    static int[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        dist = new int[n+1];
        graph = new ArrayList[n+1];
        for (int i = 0; i < n+1; i++) {
            graph[i] = new ArrayList<>();
            dist[i] = -1;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            graph[s].add(e);
        }
        //System.out.println(Arrays.toString(graph));
        bfs(x);
        //System.out.println(Arrays.toString(dist));

        boolean check = false;
        for (int i = 1; i < n+1; i++) {
            if (dist[i] == k) {
                System.out.println(i);
                check=true;
            }
        }
        if (!check) {
            System.out.println(-1);
        }
    }

    public static void bfs(int start) {
        dist[start] = 0;

        Queue<Integer> q = new LinkedList<>();
        q.offer(start);

        while (!q.isEmpty()) {
            int temp = q.poll();
            for (int next : graph[temp]) {
                if (dist[next] == -1) {
                    dist[next] = dist[temp]+1;
                    q.offer(next);
                }
            }
        }
    }
}