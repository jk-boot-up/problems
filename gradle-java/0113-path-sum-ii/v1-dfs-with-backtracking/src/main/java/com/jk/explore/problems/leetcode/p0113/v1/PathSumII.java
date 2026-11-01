package com.jk.explore.problems.leetcode.p0113.v1;

import java.util.*;

public class PathSumII {

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> out = new ArrayList<>();
        dfs(root, targetSum, new ArrayList<>(), out);
        return out;
    }

    private void dfs(TreeNode n, int remaining, List<Integer> path, List<List<Integer>> out) {
        if (n == null) return;
        path.add(n.val);
        remaining -= n.val;
        if (n.left == null && n.right == null && remaining == 0) out.add(new ArrayList<>(path));
        dfs(n.left, remaining, path, out);
        dfs(n.right, remaining, path, out);
        path.removeLast();
    }
}
