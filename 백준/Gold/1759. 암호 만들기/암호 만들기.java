import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static String[] txt;
    static boolean[] check;
    static int L, C;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        
        txt = new String[C];
        check = new boolean[C];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            txt[i] = st.nextToken();
        }
        Arrays.sort(txt);

        combination("", 0, 0, 0, 0);
    }
    
    static void combination(String ans, int idx, int cnt, int flag1, int flag2) {
        String checkTxt = "aeiou";

        if(cnt > 1) {
            int size = ans.length();
            if (ans.charAt(size-2) > ans.charAt(size-1)) return;
        }
        if(cnt == L) {
            if (flag1 == 0 || flag2 < 2) return;
            System.out.println(ans);
            return;
        }

        for (int i = idx; i < C; i++) {
            if(!check[i]) {
                check[i] = true;
                if (checkTxt.contains(txt[i])) {
                    combination(ans + txt[i], idx+1, cnt+1, flag1+1, flag2);
                } else {
                    combination(ans + txt[i], idx+1, cnt+1, flag1, flag2+1);
                }
                check[i] = false;
            }
        }
    }
}
