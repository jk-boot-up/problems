package com.jk.explore.problems.leetcode.p0559.v1;

import java.util.*;

public class NaryMaxDepth {

    public static final class Node {
        public int val;
        public List<Node> children;

        public Node(int val, Node... children) {
            this.val = val;
            this.children = new ArrayList<>(List.of(children));
        }
    }

    public int maxDepth(Node root) {
        if (root == null) return 0;
        int deepest = 0;
        for (Node child : root.children) deepest = Math.max(deepest, maxDepth(child));
        return deepest + 1;
    }
}
