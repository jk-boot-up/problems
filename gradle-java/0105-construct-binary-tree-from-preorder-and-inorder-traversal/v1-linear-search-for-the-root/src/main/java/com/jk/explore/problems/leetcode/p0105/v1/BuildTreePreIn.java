package com.jk.explore.problems.leetcode.p0105.v1;

import java.util.*;

public class BuildTreePreIn {

    private int next;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        next = 0;
        return build(preorder, inorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int[] inorder, int lo, int hi) {
        if (lo > hi) return null;
        TreeNode root = new TreeNode(preorder[next++]);
        int m = lo;
        while (inorder[m] != root.val) m++;
        root.left = build(preorder, inorder, lo, m - 1);
        root.right = build(preorder, inorder, m + 1, hi);
        return root;
    }
}
