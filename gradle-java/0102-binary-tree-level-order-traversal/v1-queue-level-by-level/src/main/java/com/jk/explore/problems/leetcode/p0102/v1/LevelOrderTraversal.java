package com.jk.explore.problems.leetcode.p0102.v1;

import java.util.*;

public class LevelOrderTraversal {

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> out = new ArrayList<>();
        if (root == null) return out;
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                level.add(n.val);
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
            out.add(level);
        }
        return out;
    }
}
