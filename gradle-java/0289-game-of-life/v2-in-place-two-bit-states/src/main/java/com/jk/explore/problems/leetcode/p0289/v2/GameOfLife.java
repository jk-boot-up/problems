package com.jk.explore.problems.leetcode.p0289.v2;

import java.util.*;

public class GameOfLife {

    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int live = 0;
                for (int di = -1; di <= 1; di++) {
                    for (int dj = -1; dj <= 1; dj++) {
                        if ((di != 0 || dj != 0) && i + di >= 0 && i + di < m && j + dj >= 0 && j + dj < n) {
                            live += board[i + di][j + dj] & 1;
                        }
                    }
                }
                if (live == 3 || (live == 2 && (board[i][j] & 1) == 1)) {
                    board[i][j] |= 2;
                }
            }
        }
        for (int[] row : board) {
            for (int j = 0; j < n; j++) row[j] >>= 1;
        }
    }
}
