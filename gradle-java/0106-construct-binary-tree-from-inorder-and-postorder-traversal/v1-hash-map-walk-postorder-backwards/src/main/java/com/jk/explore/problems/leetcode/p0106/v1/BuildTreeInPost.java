package com.jk.explore.problems.leetcode.p0106.v1;

import java.util.*;

public class BuildTreeInPost {

    private int next;
    private MyHashMap<Integer, Integer> inorderIndex;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        inorderIndex = new MyHashMap<>();
        for (int i = 0; i < inorder.length; i++) inorderIndex.put(inorder[i], i);
        next = postorder.length - 1;
        return build(postorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] postorder, int lo, int hi) {
        if (lo > hi) return null;
        TreeNode root = new TreeNode(postorder[next--]);
        int m = inorderIndex.get(root.val);
        root.right = build(postorder, m + 1, hi);
        root.left = build(postorder, lo, m - 1);
        return root;
    }
}
