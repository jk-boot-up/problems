package com.jk.explore.problems.leetcode.p0572.v1;

import java.util.*;

public class SubtreeOfAnotherTree {

    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) return false;
        return same(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean same(TreeNode a, TreeNode b) {
        if (a == null || b == null) return a == b;
        return a.val == b.val && same(a.left, b.left) && same(a.right, b.right);
    }
}
