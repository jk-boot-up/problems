package com.jk.explore.problems.leetcode.p0583.v1;

import java.util.*;

public class DeleteOperationTwoStrings {

    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[] dp = new int[n + 1];
        for (int i = 1; i <= m; i++) {
            int diag = 0;
            for (int j = 1; j <= n; j++) {
                int up = dp[j];
                dp[j] = word1.charAt(i - 1) == word2.charAt(j - 1) ? diag + 1 : Math.max(dp[j], dp[j - 1]);
                diag = up;
            }
        }
        return m + n - 2 * dp[n];
    }
}
