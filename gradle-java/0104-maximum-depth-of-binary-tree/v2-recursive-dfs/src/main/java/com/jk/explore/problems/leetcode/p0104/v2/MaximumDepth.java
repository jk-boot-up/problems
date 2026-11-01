package com.jk.explore.problems.leetcode.p0104.v2;

import java.util.*;

public class MaximumDepth {

    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
