package com.jk.explore.problems.leetcode.p0530.v1;

import java.util.*;

public class MinimumDifferenceBST {

    private Integer prev;
    private int best;

    public int getMinimumDifference(TreeNode root) {
        prev = null;
        best = Integer.MAX_VALUE;
        inorder(root);
        return best;
    }

    private void inorder(TreeNode n) {
        if (n == null) return;
        inorder(n.left);
        if (prev != null) best = Math.min(best, n.val - prev);
        prev = n.val;
        inorder(n.right);
    }
}
