package com.jk.explore.problems.leetcode.p0212.v1;

import java.util.*;

public class WordSearchII {

    public List<String> findWords(char[][] board, String[] words) {
        List<String> found = new ArrayList<>();
        for (String w : words) {
            if (exists(board, w) && !found.contains(w)) found.add(w);
        }
        return found;
    }

    private boolean exists(char[][] board, String word) {
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (dfs(board, r, c, word, 0)) return true;
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, int r, int c, String word, int i) {
        if (i == word.length()) return true;
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length || board[r][c] != word.charAt(i)) return false;
        char ch = board[r][c];
        board[r][c] = '#';
        boolean ok = dfs(board, r + 1, c, word, i + 1) || dfs(board, r - 1, c, word, i + 1)
                || dfs(board, r, c + 1, word, i + 1) || dfs(board, r, c - 1, word, i + 1);
        board[r][c] = ch;
        return ok;
    }
}
