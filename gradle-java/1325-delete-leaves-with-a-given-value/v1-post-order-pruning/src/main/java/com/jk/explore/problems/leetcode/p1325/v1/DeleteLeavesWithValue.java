package com.jk.explore.problems.leetcode.p1325.v1;

import java.util.*;

public class DeleteLeavesWithValue {

    public TreeNode removeLeafNodes(TreeNode root, int target) {
        if (root == null) return null;
        root.left = removeLeafNodes(root.left, target);
        root.right = removeLeafNodes(root.right, target);
        return root.left == null && root.right == null && root.val == target ? null : root;
    }
}
