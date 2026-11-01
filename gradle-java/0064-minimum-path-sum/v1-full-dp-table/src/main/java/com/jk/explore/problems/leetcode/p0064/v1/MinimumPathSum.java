package com.jk.explore.problems.leetcode.p0064.v1;

import java.util.*;

public class MinimumPathSum {

    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int best = (i == 0 && j == 0) ? 0 : Integer.MAX_VALUE;
                if (i > 0) best = Math.min(best, dp[i - 1][j]);
                if (j > 0) best = Math.min(best, dp[i][j - 1]);
                dp[i][j] = best + grid[i][j];
            }
        }
        return dp[m - 1][n - 1];
    }
}
