package com.jk.explore.problems.leetcode.p0701.v1;

import java.util.*;

public class InsertIntoBST {

    public TreeNode insertIntoBST(TreeNode root, int val) {
        TreeNode node = new TreeNode(val);
        if (root == null) return node;
        TreeNode n = root;
        while (true) {
            if (val < n.val) {
                if (n.left == null) { n.left = node; break; }
                n = n.left;
            } else {
                if (n.right == null) { n.right = node; break; }
                n = n.right;
            }
        }
        return root;
    }
}
