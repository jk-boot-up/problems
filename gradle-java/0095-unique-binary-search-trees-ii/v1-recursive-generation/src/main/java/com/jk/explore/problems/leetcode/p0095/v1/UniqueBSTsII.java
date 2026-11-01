package com.jk.explore.problems.leetcode.p0095.v1;

import java.util.*;

public class UniqueBSTsII {

    public List<TreeNode> generateTrees(int n) {
        return build(1, n);
    }

    private List<TreeNode> build(int lo, int hi) {
        List<TreeNode> out = new ArrayList<>();
        if (lo > hi) {
            out.add(null);
            return out;
        }
        for (int r = lo; r <= hi; r++) {
            for (TreeNode left : build(lo, r - 1)) {
                for (TreeNode right : build(r + 1, hi)) out.add(new TreeNode(r, left, right));
            }
        }
        return out;
    }
}
