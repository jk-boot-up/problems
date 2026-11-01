package com.jk.explore.problems.leetcode.p0098.v1;

import java.util.*;

public class ValidateBST {

    private Integer prev;

    public boolean isValidBST(TreeNode root) {
        prev = null;
        return inorder(root);
    }

    private boolean inorder(TreeNode n) {
        if (n == null) return true;
        if (!inorder(n.left)) return false;
        if (prev != null && n.val <= prev) return false;
        prev = n.val;
        return inorder(n.right);
    }
}
