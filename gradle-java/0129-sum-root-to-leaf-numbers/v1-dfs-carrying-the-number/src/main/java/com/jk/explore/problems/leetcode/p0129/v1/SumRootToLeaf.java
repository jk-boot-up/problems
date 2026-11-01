package com.jk.explore.problems.leetcode.p0129.v1;

import java.util.*;

public class SumRootToLeaf {

    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode n, int prefix) {
        if (n == null) return 0;
        int value = prefix * 10 + n.val;
        if (n.left == null && n.right == null) return value;
        return dfs(n.left, value) + dfs(n.right, value);
    }
}
