package com.jk.explore.problems.leetcode.p0199.v1;

import java.util.*;

public class RightSideView {

    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        dfs(root, 0, out);
        return out;
    }

    private void dfs(TreeNode n, int depth, List<Integer> out) {
        if (n == null) return;
        if (depth == out.size()) out.add(n.val);
        dfs(n.right, depth + 1, out);
        dfs(n.left, depth + 1, out);
    }
}
