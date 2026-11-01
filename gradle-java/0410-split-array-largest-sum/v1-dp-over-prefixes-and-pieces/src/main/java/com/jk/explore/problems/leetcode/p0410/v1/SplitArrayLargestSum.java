package com.jk.explore.problems.leetcode.p0410.v1;

import java.util.*;

public class SplitArrayLargestSum {

    public int splitArray(int[] nums, int k) {
        int n = nums.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        long[][] best = new long[k + 1][n + 1];
        for (long[] row : best) Arrays.fill(row, Long.MAX_VALUE);
        best[0][0] = 0;
        for (int j = 1; j <= k; j++)
            for (int i = 1; i <= n; i++)
                for (int p = j - 1; p < i; p++)
                    if (best[j - 1][p] != Long.MAX_VALUE)
                        best[j][i] = Math.min(best[j][i], Math.max(best[j - 1][p], prefix[i] - prefix[p]));
        return (int) best[k][n];
    }
}
