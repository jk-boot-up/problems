package com.jk.explore.problems.leetcode.p0112.v1;

import java.util.*;

public class PathSum {

    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        int rest = targetSum - root.val;
        if (root.left == null && root.right == null) return rest == 0;
        return hasPathSum(root.left, rest) || hasPathSum(root.right, rest);
    }
}
