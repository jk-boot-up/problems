package com.jk.explore.problems.leetcode.p0687.v1;

import java.util.*;

public class LongestUnivaluePath {

    private int best;

    public int longestUnivaluePath(TreeNode root) {
        best = 0;
        arm(root);
        return best;
    }

    private int arm(TreeNode node) {
        if (node == null) return 0;
        int l = arm(node.left), r = arm(node.right);
        l = node.left != null && node.left.val == node.val ? l + 1 : 0;
        r = node.right != null && node.right.val == node.val ? r + 1 : 0;
        best = Math.max(best, l + r);
        return Math.max(l, r);
    }
}
