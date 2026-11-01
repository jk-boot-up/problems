package com.jk.explore.problems.leetcode.p0052.v2;

import java.util.*;

public class NQueensII {

    public int totalNQueens(int n) {
        return place(n, 0, 0, 0, 0);
    }

    private int place(int n, int row, int cols, int diag1, int diag2) {
        if (row == n) return 1;
        int count = 0, full = (1 << n) - 1;
        int free = ~(cols | diag1 | diag2) & full;
        while (free != 0) {
            int bit = free & -free; // lowest free column
            free -= bit;
            count += place(n, row + 1, cols | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1);
        }
        return count;
    }
}
