package com.jk.explore.problems.leetcode.p0114.v1;

import java.util.*;

public class FlattenTree {

    public void flatten(TreeNode root) {
        List<TreeNode> order = new ArrayList<>();
        preorder(root, order);
        for (int i = 0; i < order.size(); i++) {
            order.get(i).left = null;
            order.get(i).right = i + 1 < order.size() ? order.get(i + 1) : null;
        }
    }

    private void preorder(TreeNode n, List<TreeNode> out) {
        if (n == null) return;
        out.add(n);
        preorder(n.left, out);
        preorder(n.right, out);
    }
}
