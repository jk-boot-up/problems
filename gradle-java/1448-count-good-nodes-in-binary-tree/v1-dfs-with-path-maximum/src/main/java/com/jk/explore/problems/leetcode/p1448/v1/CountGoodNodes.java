package com.jk.explore.problems.leetcode.p1448.v1;

import java.util.*;

public class CountGoodNodes {

    public int goodNodes(TreeNode root) {
        return dfs(root, Integer.MIN_VALUE);
    }

    private int dfs(TreeNode n, int maxSoFar) {
        if (n == null) return 0;
        int good = n.val >= maxSoFar ? 1 : 0;
        int m = Math.max(maxSoFar, n.val);
        return good + dfs(n.left, m) + dfs(n.right, m);
    }
}
