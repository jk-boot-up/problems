package com.jk.explore.problems.leetcode.p0173.v1;

import java.util.*;

public class BSTIterator {

    private final List<Integer> values = new ArrayList<>();
    private int index;

    public BSTIterator(TreeNode root) {
        inorder(root);
    }

    private void inorder(TreeNode n) {
        if (n == null) return;
        inorder(n.left);
        values.add(n.val);
        inorder(n.right);
    }

    public int next() {
        return values.get(index++);
    }

    public boolean hasNext() {
        return index < values.size();
    }
}
