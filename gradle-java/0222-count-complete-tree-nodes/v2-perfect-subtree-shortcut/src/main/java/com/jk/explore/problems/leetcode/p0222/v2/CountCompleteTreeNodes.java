package com.jk.explore.problems.leetcode.p0222.v2;

import java.util.*;

public class CountCompleteTreeNodes {

    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        int left = 0, right = 0;
        for (TreeNode n = root; n != null; n = n.left) left++;
        for (TreeNode n = root; n != null; n = n.right) right++;
        if (left == right) return (1 << left) - 1;
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
}
