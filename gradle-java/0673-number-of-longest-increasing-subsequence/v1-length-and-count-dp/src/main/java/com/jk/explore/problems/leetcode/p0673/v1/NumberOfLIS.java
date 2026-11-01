package com.jk.explore.problems.leetcode.p0673.v1;

import java.util.*;

public class NumberOfLIS {

    public int findNumberOfLIS(int[] nums) {
        int n = nums.length, best = 0, total = 0;
        int[] len = new int[n], cnt = new int[n];
        for (int i = 0; i < n; i++) {
            len[i] = 1;
            cnt[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] >= nums[i]) continue;
                if (len[j] + 1 > len[i]) {
                    len[i] = len[j] + 1;
                    cnt[i] = cnt[j];
                } else if (len[j] + 1 == len[i]) cnt[i] += cnt[j];
            }
            if (len[i] > best) {
                best = len[i];
                total = cnt[i];
            } else if (len[i] == best) total += cnt[i];
        }
        return total;
    }
}
