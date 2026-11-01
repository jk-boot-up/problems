package com.jk.explore.problems.leetcode.p1572.v1;

import java.util.*;

public class MatrixDiagonalSum {

    public int diagonalSum(int[][] mat) {
        int n = mat.length, sum = 0;
        for (int i = 0; i < n; i++) {
            sum += mat[i][i];
            if (i != n - 1 - i) sum += mat[i][n - 1 - i];
        }
        return sum;
    }
}
