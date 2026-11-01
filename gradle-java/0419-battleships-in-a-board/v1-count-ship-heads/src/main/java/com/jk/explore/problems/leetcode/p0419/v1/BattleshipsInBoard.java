package com.jk.explore.problems.leetcode.p0419.v1;

import java.util.*;

public class BattleshipsInBoard {

    public int countBattleships(char[][] board) {
        int count = 0;
        for (int r = 0; r < board.length; r++)
            for (int c = 0; c < board[0].length; c++) {
                if (board[r][c] != 'X') continue;
                if (r > 0 && board[r - 1][c] == 'X') continue;
                if (c > 0 && board[r][c - 1] == 'X') continue;
                count++;
            }
        return count;
    }
}
