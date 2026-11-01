package com.jk.explore.problems.leetcode.p0226.v1;

import java.util.*;

public class InvertBinaryTree {

    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        while (!queue.isEmpty()) {
            TreeNode n = queue.poll();
            TreeNode t = n.left;
            n.left = n.right;
            n.right = t;
            if (n.left != null) queue.add(n.left);
            if (n.right != null) queue.add(n.right);
        }
        return root;
    }
}
