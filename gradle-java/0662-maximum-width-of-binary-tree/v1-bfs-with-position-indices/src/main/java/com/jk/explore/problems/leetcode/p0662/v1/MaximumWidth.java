package com.jk.explore.problems.leetcode.p0662.v1;

import java.util.*;

public class MaximumWidth {

    public int widthOfBinaryTree(TreeNode root) {
        Deque<Object[]> queue = new ArrayDeque<>();
        queue.add(new Object[]{root, 0L});
        long best = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            long first = (long) queue.peekFirst()[1], last = first;
            for (int i = 0; i < size; i++) {
                Object[] item = queue.poll();
                TreeNode n = (TreeNode) item[0];
                long pos = (long) item[1] - first;
                last = pos;
                if (n.left != null) queue.add(new Object[]{n.left, 2 * pos});
                if (n.right != null) queue.add(new Object[]{n.right, 2 * pos + 1});
            }
            best = Math.max(best, last + 1);
        }
        return (int) best;
    }
}
