package com.jk.explore.problems.leetcode.p0230.v2;

import java.util.*;

/** Binary tree node used by the LeetCode tree problems. */
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;

    public TreeNode(int val) { this.val = val; }

    public TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left = left; this.right = right; }

    /** Builds a tree from LeetCode level-order notation, e.g. of(3, 9, 20, null, null, 15, 7). */
    public static TreeNode of(Integer... values) {
        if (values.length == 0 || values[0] == null) return null;
        TreeNode root = new TreeNode(values[0]);
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        int i = 1;
        while (!queue.isEmpty() && i < values.length) {
            TreeNode node = queue.poll();
            if (i < values.length && values[i] != null) { node.left = new TreeNode(values[i]); queue.add(node.left); }
            i++;
            if (i < values.length && values[i] != null) { node.right = new TreeNode(values[i]); queue.add(node.right); }
            i++;
        }
        return root;
    }

    /** Serializes a tree to LeetCode level-order notation with trailing nulls removed. */
    public static List<Integer> toList(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        Deque<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node == null) { out.add(null); continue; }
            out.add(node.val);
            queue.add(node.left);
            queue.add(node.right);
        }
        while (!out.isEmpty() && out.getLast() == null) out.removeLast();
        return out;
    }
}
