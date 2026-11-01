package com.jk.explore.problems.leetcode.p0783.v1;

import java.util.*;

public class MinimumDistanceBST {

    public int minDiffInBST(TreeNode root) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode cur = root;
        Integer prev = null;
        int best = Integer.MAX_VALUE;
        while (cur != null || !stack.isEmpty()) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            if (prev != null) best = Math.min(best, cur.val - prev);
            prev = cur.val;
            cur = cur.right;
        }
        return best;
    }
}
