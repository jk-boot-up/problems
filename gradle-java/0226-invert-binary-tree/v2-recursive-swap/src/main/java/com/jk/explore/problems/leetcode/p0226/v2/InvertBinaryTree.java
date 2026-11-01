package com.jk.explore.problems.leetcode.p0226.v2;

import java.util.*;

public class InvertBinaryTree {

    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        TreeNode left = invertTree(root.left);
        root.left = invertTree(root.right);
        root.right = left;
        return root;
    }
}
