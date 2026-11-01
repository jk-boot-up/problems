package com.jk.explore.problems.leetcode.p0117.v2;

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
        Node levelStart = root;
        while (levelStart != null) {
            Node dummy = new Node(0), tail = dummy;
            for (Node n = levelStart; n != null; n = n.next) {
                if (n.left != null) { tail.next = n.left; tail = tail.next; }
                if (n.right != null) { tail.next = n.right; tail = tail.next; }
            }
            levelStart = dummy.next;
        }
        return root;
    }
}
