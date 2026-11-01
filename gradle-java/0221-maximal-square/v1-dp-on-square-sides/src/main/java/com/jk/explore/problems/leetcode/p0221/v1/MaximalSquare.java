package com.jk.explore.problems.leetcode.p0221.v1;

import java.util.*;

public class MaximalSquare {

    public int maximalSquare(char[][] matrix) {
        int m = matrix.length, n = matrix[0].length, best = 0;
        int[][] side = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i - 1][j - 1] == '1') {
                    side[i][j] = 1 + Math.min(side[i - 1][j - 1], Math.min(side[i - 1][j], side[i][j - 1]));
                    best = Math.max(best, side[i][j]);
                }
            }
        }
        return best * best;
    }
}
