import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static class Point {
        int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int n, m;
    static int[][] map;
    static ArrayList<Point> person;
    static ArrayList<Point> chicken;
    static int ans;
    static boolean[] check;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][n];
        person = new ArrayList<>();
        chicken = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());

                if (map[i][j] == 1) {
                    person.add(new Point(i, j));
                } else if (map[i][j] == 2) {
                    chicken.add(new Point(i, j));
                }
            }
        }

        ans = Integer.MAX_VALUE;
        check = new boolean[chicken.size()];

        DFS(0, 0);
        System.out.println(ans);
    }

    static void DFS(int s, int cnt) {
        if (cnt == m) {
            int res = 0;

            for (int i = 0; i < person.size(); i++) {
                int temp = Integer.MAX_VALUE;
                Point p = person.get(i);

                for (int j = 0; j < chicken.size(); j++) {
                    if (check[j]) {
                        Point c = chicken.get(j);
                        int dist = Math.abs(p.x - c.x) + Math.abs(p.y - c.y);
                        temp = Math.min(temp, dist);
                    }
                }
                res += temp;
            }
            ans = Math.min(res, ans);
            return;
        }

        for (int i = s; i < chicken.size(); i++) {
            check[i] = true;
            DFS(i+1, cnt+1);
            check[i] = false;
        }
    }
}