package com.jk.explore.problems.leetcode.p0145.v1;

import java.util.*;

public class PostorderTraversal {

    public List<Integer> postorderTraversal(TreeNode root) {
        LinkedList<Integer> out = new LinkedList<>();
        if (root == null) return out;
        Deque<TreeNode> stack = new ArrayDeque<>(List.of(root));
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            out.addFirst(n.val);
            if (n.left != null) stack.push(n.left);
            if (n.right != null) stack.push(n.right);
        }
        return out;
    }
}
