package com.jk.explore.problems.leetcode.p0538.v1;

import java.util.*;

public class BSTToGreaterTree {

    private int sum;

    public TreeNode convertBST(TreeNode root) {
        sum = 0;
        walk(root);
        return root;
    }

    private void walk(TreeNode node) {
        if (node == null) return;
        walk(node.right);
        sum += node.val;
        node.val = sum;
        walk(node.left);
    }
}
