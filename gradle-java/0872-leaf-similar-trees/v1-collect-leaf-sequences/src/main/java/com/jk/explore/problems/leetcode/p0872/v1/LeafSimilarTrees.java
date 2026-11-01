package com.jk.explore.problems.leetcode.p0872.v1;

import java.util.*;

public class LeafSimilarTrees {

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> a = new ArrayList<>(), b = new ArrayList<>();
        leaves(root1, a);
        leaves(root2, b);
        return a.equals(b);
    }

    private void leaves(TreeNode n, List<Integer> out) {
        if (n == null) return;
        if (n.left == null && n.right == null) out.add(n.val);
        leaves(n.left, out);
        leaves(n.right, out);
    }
}
