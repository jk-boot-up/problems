package com.jk.explore.problems.leetcode.p0289.v1;

import java.util.*;

public class GameOfLife {

    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;
        int[][] old = new int[m][];
        for (int i = 0; i < m; i++) old[i] = board[i].clone();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int live = 0;
                for (int di = -1; di <= 1; di++) {
                    for (int dj = -1; dj <= 1; dj++) {
                        if ((di != 0 || dj != 0) && i + di >= 0 && i + di < m && j + dj >= 0 && j + dj < n) {
                            live += old[i + di][j + dj];
                        }
                    }
                }
                board[i][j] = (live == 3 || (live == 2 && old[i][j] == 1)) ? 1 : 0;
            }
        }
    }
}
