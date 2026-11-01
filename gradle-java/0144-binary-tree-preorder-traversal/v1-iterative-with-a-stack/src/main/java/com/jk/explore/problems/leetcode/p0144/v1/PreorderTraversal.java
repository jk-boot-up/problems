package com.jk.explore.problems.leetcode.p0144.v1;

import java.util.*;

public class PreorderTraversal {

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> stack = new ArrayDeque<>(List.of(root));
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            out.add(n.val);
            if (n.right != null) stack.push(n.right);
            if (n.left != null) stack.push(n.left);
        }
        return out;
    }
}
