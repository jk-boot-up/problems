package com.jk.explore.problems.leetcode.p0097.v2;

import java.util.*;

public class InterleavingString {

    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length(), n = s2.length();
        if (m + n != s3.length()) return false;
        boolean[] ok = new boolean[n + 1];
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 && j == 0) ok[j] = true;
                else {
                    boolean fromS1 = i > 0 && ok[j] && s1.charAt(i - 1) == s3.charAt(i + j - 1);
                    boolean fromS2 = j > 0 && ok[j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1);
                    ok[j] = fromS1 || fromS2;
                }
            }
        }
        return ok[n];
    }
}
