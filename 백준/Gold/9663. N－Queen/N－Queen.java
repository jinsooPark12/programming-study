// N x N 체스판에 퀸 N개 배치 -> 백트레킹
// 퀸이 서로 공격할 수 없는 위치 계산
// -> 선택한 퀸 기준 왼쪽 대각선 방향, 위쪽 방향, 오른쪽 대각선 방향 검사

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int n;
    static int[] arr;
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];

        queen(0);
        System.out.println(ans);
    }

    static void queen(int cnt) {
        if(cnt == n) {
            ans++;
            return;
        }

        for (int i = 0; i < n; i++) {
            arr[cnt] = i;
            if (isSafe(cnt)) {
                queen(cnt+1);
            }
        }
    }

    static boolean isSafe(int x) {
        for (int i = 0; i < x; i++) {
            if(arr[i] == arr[x])
                return false;
            else if(Math.abs(x-i) == Math.abs(arr[x]-arr[i]))
                return false;
        }
        return true;
    }
}
