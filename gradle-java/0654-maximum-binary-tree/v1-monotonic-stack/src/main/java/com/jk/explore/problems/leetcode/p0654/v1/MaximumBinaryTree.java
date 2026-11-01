package com.jk.explore.problems.leetcode.p0654.v1;

import java.util.*;

public class MaximumBinaryTree {

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        for (int x : nums) {
            TreeNode node = new TreeNode(x);
            while (!stack.isEmpty() && stack.peek().val < x) node.left = stack.pop();
            if (!stack.isEmpty()) stack.peek().right = node;
            stack.push(node);
        }
        return stack.peekLast();
    }
}
