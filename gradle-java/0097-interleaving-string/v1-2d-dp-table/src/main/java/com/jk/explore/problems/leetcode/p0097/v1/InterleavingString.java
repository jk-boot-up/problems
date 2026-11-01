package com.jk.explore.problems.leetcode.p0097.v1;

import java.util.*;

public class InterleavingString {

    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length(), n = s2.length();
        if (m + n != s3.length()) return false;
        boolean[][] ok = new boolean[m + 1][n + 1];
        ok[0][0] = true;
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i > 0 && ok[i - 1][j] && s1.charAt(i - 1) == s3.charAt(i + j - 1)) ok[i][j] = true;
                if (j > 0 && ok[i][j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1)) ok[i][j] = true;
            }
        }
        return ok[m][n];
    }
}
