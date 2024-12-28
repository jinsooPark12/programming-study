import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static class tomato {
        int x, y;

        public tomato(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int n, m;
    static int[][] map;
    static Queue<tomato> q;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    static int ans = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        q = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1) {
                    q.offer(new tomato(i, j));
                }
            }
        }

        bfs();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 0) {
                    System.out.println(-1);
                    return;
                }
            }
        }
        System.out.println(ans-1);
    }

    static void bfs() {
        while (!q.isEmpty()) {
            tomato cur = q.poll();
            int curX = cur.x;
            int curY = cur.y;

            for (int i = 0; i < 4; i++) {
                int nx = curX + dx[i];
                int ny = curY + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (map[nx][ny] == 0) {
                        map[nx][ny] = map[curX][curY] + 1;
                        q.offer(new tomato(nx, ny));
                        ans = Math.max(map[nx][ny], ans);
                    }
                }
            }
        }
    }
}
