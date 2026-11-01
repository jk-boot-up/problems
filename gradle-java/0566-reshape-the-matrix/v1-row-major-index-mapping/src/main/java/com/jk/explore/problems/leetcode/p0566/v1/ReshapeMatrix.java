package com.jk.explore.problems.leetcode.p0566.v1;

import java.util.*;

public class ReshapeMatrix {

    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length, n = mat[0].length;
        if (m * n != r * c) return mat;
        int[][] out = new int[r][c];
        for (int k = 0; k < m * n; k++) out[k / c][k % c] = mat[k / n][k % n];
        return out;
    }
}
