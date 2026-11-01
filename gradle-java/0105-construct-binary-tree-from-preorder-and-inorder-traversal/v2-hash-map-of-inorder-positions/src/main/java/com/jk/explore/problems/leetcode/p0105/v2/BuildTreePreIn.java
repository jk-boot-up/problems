package com.jk.explore.problems.leetcode.p0105.v2;

import java.util.*;

public class BuildTreePreIn {

    private int next;
    private MyHashMap<Integer, Integer> inorderIndex;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        inorderIndex = new MyHashMap<>();
        for (int i = 0; i < inorder.length; i++) inorderIndex.put(inorder[i], i);
        next = 0;
        return build(preorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int lo, int hi) {
        if (lo > hi) return null;
        TreeNode root = new TreeNode(preorder[next++]);
        int m = inorderIndex.get(root.val);
        root.left = build(preorder, lo, m - 1);
        root.right = build(preorder, m + 1, hi);
        return root;
    }
}
