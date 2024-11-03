import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n;
    static int[] value;
    static int[] answer;
    static int[] parentNum;
    static ArrayList<ArrayList<Integer>> graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        value = new int[n+1];
        answer = new int[n+1];
        parentNum = new int[n+1];
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            value[i] = Integer.parseInt(st.nextToken());

            while (st.hasMoreTokens()) {
                int num = Integer.parseInt(st.nextToken());

                if (num == -1) {
                    break;
                }

                graph.get(num).add(i);
                parentNum[i]++;
            }
        }

        topologicalSort();

        for (int i = 1; i <= n; i++) {
            System.out.println(answer[i]);
        }
    }

    static void topologicalSort() {
        Queue<Integer> q = new LinkedList<>();

        for (int i = 1; i <= n; i++) {
            if (parentNum[i] == 0) {
                q.offer(i);
            }
        }

        while (!q.isEmpty()) {
            int v = q.poll();
            answer[v] += value[v];

            for (int i = 0; i < graph.get(v).size(); i++) {
                int nextV = graph.get(v).get(i);

                parentNum[nextV]--;
                if (parentNum[nextV] == 0) {
                    q.offer(nextV);
                }

                answer[nextV] = Math.max(answer[nextV], answer[v]);
            }
        }
    }
}