package com.jk.explore.problems.leetcode.p0116.v1;

import java.util.*;

public class PopulatingNextRightPerfect {

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
        for (Node leftmost = root; leftmost != null && leftmost.left != null; leftmost = leftmost.left) {
            for (Node n = leftmost; n != null; n = n.next) {
                n.left.next = n.right;
                if (n.next != null) n.right.next = n.next.left;
            }
        }
        return root;
    }
}
