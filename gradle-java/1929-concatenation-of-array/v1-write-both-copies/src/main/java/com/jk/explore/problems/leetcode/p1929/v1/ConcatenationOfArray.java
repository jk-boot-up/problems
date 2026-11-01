package com.jk.explore.problems.leetcode.p1929.v1;

import java.util.*;

public class ConcatenationOfArray {

    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] ans = new int[2 * n];
        for (int i = 0; i < n; i++) ans[i] = ans[i + n] = nums[i];
        return ans;
    }
}
