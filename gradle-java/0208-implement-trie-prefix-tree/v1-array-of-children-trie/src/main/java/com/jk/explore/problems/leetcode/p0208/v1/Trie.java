package com.jk.explore.problems.leetcode.p0208.v1;

import java.util.*;

public class Trie {

    private static final class Node {
        final Node[] children = new Node[26];
        boolean end;
    }

    private final Node root = new Node();

    public void insert(String word) {
        Node n = root;
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (n.children[i] == null) n.children[i] = new Node();
            n = n.children[i];
        }
        n.end = true;
    }

    public boolean search(String word) {
        Node n = walk(word);
        return n != null && n.end;
    }

    public boolean startsWith(String prefix) {
        return walk(prefix) != null;
    }

    private Node walk(String s) {
        Node n = root;
        for (char c : s.toCharArray()) {
            n = n.children[c - 'a'];
            if (n == null) return null;
        }
        return n;
    }
}
