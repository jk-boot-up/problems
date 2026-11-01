package com.jk.explore.problems.leetcode.p0173.v2;

import java.util.*;

public class BSTIterator {

    private final Deque<TreeNode> stack = new ArrayDeque<>();

    public BSTIterator(TreeNode root) {
        pushLeft(root);
    }

    public int next() {
        TreeNode n = stack.pop();
        pushLeft(n.right);
        return n.val;
    }

    public boolean hasNext() {
        return !stack.isEmpty();
    }

    private void pushLeft(TreeNode n) {
        for (; n != null; n = n.left) stack.push(n);
    }
}
