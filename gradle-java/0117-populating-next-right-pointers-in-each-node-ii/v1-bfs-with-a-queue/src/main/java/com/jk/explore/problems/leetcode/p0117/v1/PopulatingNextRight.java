package com.jk.explore.problems.leetcode.p0117.v1;

import java.util.*;

public class PopulatingNextRight {

    /** Tree node with a next pointer. */
    public static class Node {
        public int val;
        public Node left, right, next;

        public Node(int val) { this.val = val; }

        public Node(int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public Node connect(Node root) {
        if (root == null) return null;
        Deque<Node> queue = new ArrayDeque<>(List.of(root));
        while (!queue.isEmpty()) {
            Node prev = null;
            for (int size = queue.size(); size > 0; size--) {
                Node n = queue.poll();
                if (prev != null) prev.next = n;
                prev = n;
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
        }
        return root;
    }
}
