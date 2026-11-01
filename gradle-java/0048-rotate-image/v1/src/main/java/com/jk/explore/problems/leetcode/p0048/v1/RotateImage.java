package com.jk.explore.problems.leetcode.p0048.v1;

import java.util.*;

public class RotateImage {

    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int[][] rotated = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                rotated[j][n - 1 - i] = matrix[i][j];
            }
        }
        for (int i = 0; i < n; i++) {
            matrix[i] = rotated[i].clone();
        }
    }
}
