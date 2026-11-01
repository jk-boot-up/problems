package com.jk.explore.problems.leetcode.p0337.v1;

import java.util.*;

public class HouseRobberIII {

    public int rob(TreeNode root) {
        int[] r = dfs(root);
        return Math.max(r[0], r[1]);
    }

    /** Returns {best if this node is robbed, best if it is not}. */
    private int[] dfs(TreeNode n) {
        if (n == null) return new int[]{0, 0};
        int[] l = dfs(n.left), r = dfs(n.right);
        int take = n.val + l[1] + r[1];
        int skip = Math.max(l[0], l[1]) + Math.max(r[0], r[1]);
        return new int[]{take, skip};
    }
}
