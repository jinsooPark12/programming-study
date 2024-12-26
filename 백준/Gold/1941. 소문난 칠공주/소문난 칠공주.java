import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    static char[][] map;
    static int ans = 0;
    static boolean[] visited;
    static int[] dr = {1,-1,0,0};
    static int[] dc = {0,0,1,-1};
    static int[] selected = new int[7];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        map = new char[5][5];

        for (int i = 0; i < 5; i++) {
            map[i] = br.readLine().toCharArray();
        }
        backTracking(0, 0, 0);
        System.out.println(ans);
    }

    static void backTracking(int depth, int numY, int start) {
        if (numY >= 4) return;

        if (depth == 7) {
            visited = new boolean[7];
            BFS();
            return;
        }

        for (int i = start; i < 25; i++) {
            selected[depth] = i;
            if (map[i/5][i%5] == 'Y') {
                backTracking(depth+1, numY+1, i+1);
            } else {
                backTracking(depth+1, numY, i+1);
            }
        }
    }

    static void BFS() {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {selected[0] / 5, selected[0] % 5});
        visited[0] = true;
        int conn = 1;

        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0];
            int c = cur[1];

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                int ni = nr*5 + nc;

                if (!isValid(nr, nc)) continue;

                for (int j = 0; j < 7; j++) {
                    if (!visited[j] && selected[j]==ni) {
                        q.add(new int[] {nr, nc});
                        visited[j] = true;
                        conn++;
                    }
                }
            }
        }
        if (conn == 7) ans++;
    }

    static boolean isValid(int r, int c) {
        if (r >= 0 && r < 5 && c >= 0 && c < 5) return true;
        return false;
    }
}
