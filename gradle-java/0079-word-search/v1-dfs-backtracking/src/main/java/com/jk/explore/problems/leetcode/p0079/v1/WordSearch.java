package com.jk.explore.problems.leetcode.p0079.v1;

import java.util.*;

public class WordSearch {

    public boolean exist(char[][] board, String word) {
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (dfs(board, r, c, word, 0)) return true;
            }
        }
        return false;
    }

    private boolean dfs(char[][] b, int r, int c, String word, int i) {
        if (i == word.length()) return true;
        if (r < 0 || c < 0 || r >= b.length || c >= b[0].length || b[r][c] != word.charAt(i)) return false;
        char ch = b[r][c];
        b[r][c] = '#';
        boolean found = dfs(b, r + 1, c, word, i + 1) || dfs(b, r - 1, c, word, i + 1)
                || dfs(b, r, c + 1, word, i + 1) || dfs(b, r, c - 1, word, i + 1);
        b[r][c] = ch;
        return found;
    }
}
