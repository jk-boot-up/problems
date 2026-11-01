package com.jk.explore.problems.leetcode.p0437.v1;

import java.util.*;

public class PathSumIII {

    private final MyHashMap<Long, Integer> prefix = new MyHashMap<>();

    public int pathSum(TreeNode root, int targetSum) {
        prefix.put(0L, 1);
        return dfs(root, 0L, targetSum);
    }

    private int dfs(TreeNode n, long sum, int target) {
        if (n == null) return 0;
        sum += n.val;
        int count = prefix.getOrDefault(sum - target, 0);
        prefix.merge(sum, 1, Integer::sum);
        count += dfs(n.left, sum, target) + dfs(n.right, sum, target);
        prefix.merge(sum, -1, Integer::sum);
        return count;
    }
}
