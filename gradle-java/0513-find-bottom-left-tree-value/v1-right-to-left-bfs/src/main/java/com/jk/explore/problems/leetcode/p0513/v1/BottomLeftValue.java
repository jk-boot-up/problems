package com.jk.explore.problems.leetcode.p0513.v1;

import java.util.*;

public class BottomLeftValue {

    public int findBottomLeftValue(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        TreeNode node = root;
        while (!queue.isEmpty()) {
            node = queue.poll();
            if (node.right != null) queue.add(node.right);
            if (node.left != null) queue.add(node.left);
        }
        return node.val;
    }
}
