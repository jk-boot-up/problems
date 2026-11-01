package com.jk.explore.problems.leetcode.p0052.v1;

import java.util.*;

public class NQueensII {

    private boolean[] col, d1, d2;

    public int totalNQueens(int n) {
        col = new boolean[n];
        d1 = new boolean[2 * n];
        d2 = new boolean[2 * n];
        return place(n, 0);
    }

    private int place(int n, int r) {
        if (r == n) return 1;
        int count = 0;
        for (int c = 0; c < n; c++) {
            if (col[c] || d1[r + c] || d2[r - c + n - 1]) continue;
            col[c] = d1[r + c] = d2[r - c + n - 1] = true;
            count += place(n, r + 1);
            col[c] = d1[r + c] = d2[r - c + n - 1] = false;
        }
        return count;
    }
}
