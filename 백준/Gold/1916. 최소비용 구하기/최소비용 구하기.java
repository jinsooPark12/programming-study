import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static final int MAX_NUM = 100_000_000;
    static int n, e, start, end;
    static ArrayList<ArrayList<Node>> graph;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        e = Integer.parseInt(br.readLine());

        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph.get(a).add(new Node(b, c));
        }

        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        System.out.println(find(start, end));
    }

    public static int find(int start, int end) {
        int[] dist = new int[n+1];
        for (int i = 0; i <= n; i++) {
            dist[i] = MAX_NUM;
        }

        PriorityQueue<Node> q = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cost, o2.cost));
        q.offer(new Node(start, 0));
        dist[start] = 0;
        while (!q.isEmpty()) {
            Node curNode = q.poll();

            if (curNode.idx == end) {
                return dist[curNode.idx];
            }
            if (dist[curNode.idx] < curNode.cost) {
                continue;
            }

            for (int i = 0; i < graph.get(curNode.idx).size(); i++) {
                Node next = graph.get(curNode.idx).get(i);
                if (dist[next.idx] > curNode.cost + next.cost) {
                    dist[next.idx] = curNode.cost + next.cost;
                    q.offer(new Node(next.idx, dist[next.idx]));
                }
            }
        }
        return -1;
    }

    static class Node {
        int idx, cost;

        public Node(int idx, int cost) {
            this.idx = idx;
            this.cost = cost;
        }
    }
}