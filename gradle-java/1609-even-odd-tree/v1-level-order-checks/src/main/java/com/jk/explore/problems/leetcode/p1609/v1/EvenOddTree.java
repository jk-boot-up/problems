package com.jk.explore.problems.leetcode.p1609.v1;

import java.util.*;

public class EvenOddTree {

    public boolean isEvenOddTree(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        for (int level = 0; !queue.isEmpty(); level++) {
            boolean even = level % 2 == 0;
            long prev = even ? Long.MIN_VALUE : Long.MAX_VALUE;
            for (int size = queue.size(); size > 0; size--) {
                TreeNode n = queue.poll();
                if (even && (n.val % 2 == 0 || n.val <= prev)) return false;
                if (!even && (n.val % 2 == 1 || n.val >= prev)) return false;
                prev = n.val;
                if (n.left != null) queue.add(n.left);
                if (n.right != null) queue.add(n.right);
            }
        }
        return true;
    }
}
