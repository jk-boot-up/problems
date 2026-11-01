package com.jk.explore.problems.leetcode.p0059.v1;

import java.util.*;

public class SpiralMatrixII {

    public int[][] generateMatrix(int n) {
        int[][] m = new int[n][n];
        int top = 0, bottom = n - 1, left = 0, right = n - 1, v = 1;
        while (v <= n * n) {
            for (int c = left; c <= right; c++) m[top][c] = v++;
            top++;
            for (int r = top; r <= bottom; r++) m[r][right] = v++;
            right--;
            for (int c = right; c >= left; c--) m[bottom][c] = v++;
            bottom--;
            for (int r = bottom; r >= top; r--) m[r][left] = v++;
            left++;
        }
        return m;
    }
}
