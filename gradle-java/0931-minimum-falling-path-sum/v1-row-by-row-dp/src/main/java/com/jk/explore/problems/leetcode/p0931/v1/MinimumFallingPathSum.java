package com.jk.explore.problems.leetcode.p0931.v1;

import java.util.*;

public class MinimumFallingPathSum {

    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int[] best = matrix[0].clone();
        for (int r = 1; r < n; r++) {
            int[] next = new int[n];
            for (int c = 0; c < n; c++) {
                int above = best[c];
                if (c > 0) above = Math.min(above, best[c - 1]);
                if (c < n - 1) above = Math.min(above, best[c + 1]);
                next[c] = matrix[r][c] + above;
            }
            best = next;
        }
        int ans = Integer.MAX_VALUE;
        for (int v : best) ans = Math.min(ans, v);
        return ans;
    }
}
