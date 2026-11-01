package com.jk.explore.problems.leetcode.p0104.v1;

import java.util.*;

public class MaximumDepth {

    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        int depth = 0;
        while (!queue.isEmpty()) {
            depth++;
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
        }
        return depth;
    }
}
