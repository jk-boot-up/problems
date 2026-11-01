package com.jk.explore.problems.leetcode.p0051.v1;

import java.util.*;

public class NQueens {

    public List<List<String>> solveNQueens(int n) {
        List<List<String>> out = new ArrayList<>();
        place(n, 0, new int[n], new boolean[n], new boolean[2 * n], new boolean[2 * n], out);
        return out;
    }

    private void place(int n, int r, int[] queens, boolean[] col, boolean[] d1, boolean[] d2, List<List<String>> out) {
        if (r == n) {
            List<String> board = new ArrayList<>();
            for (int q : queens) {
                char[] row = new char[n];
                Arrays.fill(row, '.');
                row[q] = 'Q';
                board.add(new String(row));
            }
            out.add(board);
            return;
        }
        for (int c = 0; c < n; c++) {
            if (col[c] || d1[r + c] || d2[r - c + n - 1]) continue;
            queens[r] = c;
            col[c] = d1[r + c] = d2[r - c + n - 1] = true;
            place(n, r + 1, queens, col, d1, d2, out);
            col[c] = d1[r + c] = d2[r - c + n - 1] = false;
        }
    }
}
