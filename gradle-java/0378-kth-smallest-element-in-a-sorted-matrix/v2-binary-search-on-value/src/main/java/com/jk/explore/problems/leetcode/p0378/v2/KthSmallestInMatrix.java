package com.jk.explore.problems.leetcode.p0378.v2;

import java.util.*;

public class KthSmallestInMatrix {

    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        long lo = matrix[0][0], hi = matrix[n - 1][n - 1];
        while (lo < hi) {
            long mid = Math.floorDiv(lo + hi, 2);
            if (countAtMost(matrix, mid) < k) lo = mid + 1;
            else hi = mid;
        }
        return (int) lo;
    }

    private int countAtMost(int[][] m, long x) {
        int n = m.length, row = n - 1, col = 0, count = 0;
        while (row >= 0 && col < n) {
            if (m[row][col] <= x) {
                count += row + 1;
                col++;
            } else row--;
        }
        return count;
    }
}
