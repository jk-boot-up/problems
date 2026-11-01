package com.jk.explore.problems.leetcode.p0216.v1;

import java.util.*;

public class CombinationSumIII {

    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> out = new ArrayList<>();
        dfs(1, k, n, new ArrayList<>(), out);
        return out;
    }

    private void dfs(int start, int k, int left, List<Integer> path, List<List<Integer>> out) {
        if (path.size() == k) {
            if (left == 0) out.add(new ArrayList<>(path));
            return;
        }
        for (int d = start; d <= 9 && d <= left; d++) {
            path.add(d);
            dfs(d + 1, k, left - d, path, out);
            path.remove(path.size() - 1);
        }
    }
}
