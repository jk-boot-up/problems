package com.jk.explore.problems.leetcode.p0110.v1;

import java.util.*;

public class BalancedBinaryTree {

    public boolean isBalanced(TreeNode root) {
        return height(root) >= 0;
    }

    private int height(TreeNode n) {
        if (n == null) return 0;
        int l = height(n.left);
        if (l < 0) return -1;
        int r = height(n.right);
        if (r < 0 || Math.abs(l - r) > 1) return -1;
        return 1 + Math.max(l, r);
    }
}
