package com.jk.explore.problems.leetcode.p1161.v1;

import java.util.*;

public class MaximumLevelSum {

    public int maxLevelSum(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        int best = Integer.MIN_VALUE, bestLevel = 0;
        for (int level = 1; !queue.isEmpty(); level++) {
            int sum = 0;
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                sum += n.val;
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
            if (sum > best) {
                best = sum;
                bestLevel = level;
            }
        }
        return bestLevel;
    }
}
