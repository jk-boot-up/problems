package com.jk.explore.problems.leetcode.p0212.v2;

import java.util.*;

public class WordSearchII {

    private static final class Node {
        final Node[] children = new Node[26];
        String word;
    }

    public List<String> findWords(char[][] board, String[] words) {
        Node root = new Node();
        for (String w : words) {
            Node n = root;
            for (char c : w.toCharArray()) {
                if (n.children[c - 'a'] == null) n.children[c - 'a'] = new Node();
                n = n.children[c - 'a'];
            }
            n.word = w;
        }
        List<String> found = new ArrayList<>();
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) dfs(board, r, c, root, found);
        }
        return found;
    }

    private void dfs(char[][] board, int r, int c, Node parent, List<String> found) {
        if (r < 0 || c < 0 || r >= board.length || c >= board[0].length) return;
        char ch = board[r][c];
        if (ch == '#' || parent.children[ch - 'a'] == null) return;
        Node node = parent.children[ch - 'a'];
        if (node.word != null) {
            found.add(node.word);
            node.word = null;
        }
        board[r][c] = '#';
        dfs(board, r + 1, c, node, found);
        dfs(board, r - 1, c, node, found);
        dfs(board, r, c + 1, node, found);
        dfs(board, r, c - 1, node, found);
        board[r][c] = ch;
    }
}
