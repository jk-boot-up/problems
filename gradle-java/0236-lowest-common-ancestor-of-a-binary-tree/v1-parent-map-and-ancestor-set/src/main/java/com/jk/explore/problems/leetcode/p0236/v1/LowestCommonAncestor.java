package com.jk.explore.problems.leetcode.p0236.v1;

import java.util.*;

public class LowestCommonAncestor {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        MyHashMap<TreeNode, TreeNode> parent = new MyHashMap<>();
        Deque<TreeNode> stack = new ArrayDeque<>(List.of(root));
        parent.put(root, null);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            if (n.left != null) { parent.put(n.left, n); stack.push(n.left); }
            if (n.right != null) { parent.put(n.right, n); stack.push(n.right); }
        }
        MyHashSet<TreeNode> ancestors = new MyHashSet<>();
        for (TreeNode a = p; a != null; a = parent.get(a)) ancestors.add(a);
        TreeNode b = q;
        while (!ancestors.contains(b)) b = parent.get(b);
        return b;
    }
}
