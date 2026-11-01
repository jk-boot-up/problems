package com.jk.explore.problems.leetcode.p0211.v1;

import java.util.*;

public class WordDictionary {

    private static final class Node {
        final Node[] children = new Node[26];
        boolean end;
    }

    private final Node root = new Node();

    public void addWord(String word) {
        Node n = root;
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (n.children[i] == null) n.children[i] = new Node();
            n = n.children[i];
        }
        n.end = true;
    }

    public boolean search(String word) {
        return search(word, 0, root);
    }

    private boolean search(String word, int i, Node n) {
        if (i == word.length()) return n.end;
        char c = word.charAt(i);
        if (c == '.') {
            for (Node child : n.children) {
                if (child != null && search(word, i + 1, child)) return true;
            }
            return false;
        }
        Node child = n.children[c - 'a'];
        return child != null && search(word, i + 1, child);
    }
}
