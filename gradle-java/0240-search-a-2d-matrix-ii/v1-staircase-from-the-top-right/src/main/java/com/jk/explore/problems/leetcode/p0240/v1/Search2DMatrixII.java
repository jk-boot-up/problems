package com.jk.explore.problems.leetcode.p0240.v1;

import java.util.*;

public class Search2DMatrixII {

    public boolean searchMatrix(int[][] matrix, int target) {
        int r = 0, c = matrix[0].length - 1;
        while (r < matrix.length && c >= 0) {
            int v = matrix[r][c];
            if (v == target) return true;
            if (v > target) c--; else r++;
        }
        return false;
    }
}
