import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    static class Edge implements Comparable<Edge>{
        int v, w;
        Long cost;

        public Edge(int v, int w, Long cost) {
            this.v = v;
            this.w = w;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge o) {
            if (o.cost < cost) {
                return 1;
            } else if (o.cost > cost) {
                return -1;
            }
            return 0;
        }
    }

    static int[] parent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        ArrayList<Edge> graph = new ArrayList<>();
        parent = new int[n+1];
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph.add(new Edge(a,b,(long) c));
        }
        Collections.sort(graph);

        int ans = 0;
        for (int i = 0; i < e; i++) {
            Edge curNode = graph.get(i);
            int findV = find(curNode.v);
            int findW = find(curNode.w);
            boolean flag = union(findV, findW);
            if (flag) {
                ans += curNode.cost;
            }
        }
        System.out.println(ans);
    }

    static int find(int x) {
        if (x != parent[x]) {
            return parent[x] = find(parent[x]);
        }
        return x;
    }

    static boolean union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x != y) {
            parent[x] = y;
            return true;
        }
        return false;
    }
}