package com.jk.explore.problems.leetcode.p0094.v1;

import java.util.*;

public class InorderTraversal {

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        walk(root, out);
        return out;
    }

    private void walk(TreeNode n, List<Integer> out) {
        if (n == null) return;
        walk(n.left, out);
        out.add(n.val);
        walk(n.right, out);
    }
}
