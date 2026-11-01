package com.jk.explore.problems.leetcode.p0637.v1;

import java.util.*;

public class AverageOfLevels {

    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> out = new ArrayList<>();
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        while (!queue.isEmpty()) {
            int size = queue.size();
            long sum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode n = queue.poll();
                sum += n.val;
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
            out.add((double) sum / size);
        }
        return out;
    }
}
