package com.jk.explore.problems.leetcode.p0712.v1;

import java.util.*;

public class MinimumDeleteSum {

    public int minimumDeleteSum(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[] dp = new int[n + 1];
        for (int j = 1; j <= n; j++) dp[j] = dp[j - 1] + s2.charAt(j - 1);
        for (int i = 1; i <= m; i++) {
            int diag = dp[0];
            dp[0] += s1.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                int up = dp[j];
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) dp[j] = diag;
                else dp[j] = Math.min(dp[j] + s1.charAt(i - 1), dp[j - 1] + s2.charAt(j - 1));
                diag = up;
            }
        }
        return dp[n];
    }
}
