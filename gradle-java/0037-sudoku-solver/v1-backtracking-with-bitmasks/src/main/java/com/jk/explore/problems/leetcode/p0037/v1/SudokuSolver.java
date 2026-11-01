package com.jk.explore.problems.leetcode.p0037.v1;

import java.util.*;

public class SudokuSolver {

    private final int[] rows = new int[9], cols = new int[9], boxes = new int[9];
    private final List<int[]> empty = new ArrayList<>();

    public void solveSudoku(char[][] board) {
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') empty.add(new int[]{r, c});
                else toggle(r, c, board[r][c] - '1');
            }
        }
        solve(board, 0);
    }

    private boolean solve(char[][] board, int k) {
        if (k == empty.size()) return true;
        int r = empty.get(k)[0], c = empty.get(k)[1];
        int used = rows[r] | cols[c] | boxes[(r / 3) * 3 + c / 3];
        for (int d = 0; d < 9; d++) {
            if ((used >> d & 1) == 1) continue;
            toggle(r, c, d);
            board[r][c] = (char) ('1' + d);
            if (solve(board, k + 1)) return true;
            toggle(r, c, d);
        }
        board[r][c] = '.';
        return false;
    }

    private void toggle(int r, int c, int d) {
        rows[r] ^= 1 << d;
        cols[c] ^= 1 << d;
        boxes[(r / 3) * 3 + c / 3] ^= 1 << d;
    }
}
