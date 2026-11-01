package com.jk.explore.problems.leetcode.p0111.v1;

import java.util.*;

public class MinimumDepth {

    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        for (int depth = 1; ; depth++) {
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                if (n.left == null && n.right == null) return depth;
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
        }
    }
}
