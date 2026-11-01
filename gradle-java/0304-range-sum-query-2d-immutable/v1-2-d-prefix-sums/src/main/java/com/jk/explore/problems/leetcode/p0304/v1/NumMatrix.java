package com.jk.explore.problems.leetcode.p0304.v1;

import java.util.*;

public class NumMatrix {

    private final int[][] prefix;

    public NumMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        prefix = new int[m + 1][n + 1];
        for (int r = 1; r <= m; r++)
            for (int c = 1; c <= n; c++)
                prefix[r][c] = matrix[r - 1][c - 1] + prefix[r - 1][c] + prefix[r][c - 1] - prefix[r - 1][c - 1];
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        return prefix[row2 + 1][col2 + 1] - prefix[row1][col2 + 1] - prefix[row2 + 1][col1] + prefix[row1][col1];
    }
}
