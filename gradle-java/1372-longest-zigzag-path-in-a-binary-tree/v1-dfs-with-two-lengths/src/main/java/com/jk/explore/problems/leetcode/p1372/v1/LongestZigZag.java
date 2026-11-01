package com.jk.explore.problems.leetcode.p1372.v1;

import java.util.*;

public class LongestZigZag {

    private int best;

    public int longestZigZag(TreeNode root) {
        best = 0;
        dfs(root, 0, 0);
        return best;
    }

    /** left: length of a zigzag that arrived here by a left move; right: by a right move. */
    private void dfs(TreeNode n, int left, int right) {
        if (n == null) return;
        best = Math.max(best, Math.max(left, right));
        dfs(n.left, right + 1, 0);
        dfs(n.right, 0, left + 1);
    }
}
