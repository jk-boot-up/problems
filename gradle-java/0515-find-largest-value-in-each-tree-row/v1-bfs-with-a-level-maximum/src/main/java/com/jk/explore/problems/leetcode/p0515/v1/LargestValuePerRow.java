package com.jk.explore.problems.leetcode.p0515.v1;

import java.util.*;

public class LargestValuePerRow {

    public List<Integer> largestValues(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        while (!queue.isEmpty()) {
            int best = Integer.MIN_VALUE;
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                best = Math.max(best, n.val);
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
            out.add(best);
        }
        return out;
    }
}
