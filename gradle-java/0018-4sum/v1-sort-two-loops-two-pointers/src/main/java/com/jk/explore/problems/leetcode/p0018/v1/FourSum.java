package com.jk.explore.problems.leetcode.p0018.v1;

import java.util.*;

public class FourSum {

    public List<List<Integer>> fourSum(int[] nums, int target) {
        int[] a = nums.clone();
        Arrays.sort(a);
        List<List<Integer>> out = new ArrayList<>();
        int n = a.length;
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && a[i] == a[i - 1]) continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && a[j] == a[j - 1]) continue;
                int l = j + 1, r = n - 1;
                while (l < r) {
                    long sum = (long) a[i] + a[j] + a[l] + a[r];
                    if (sum < target) l++;
                    else if (sum > target) r--;
                    else {
                        out.add(List.of(a[i], a[j], a[l], a[r]));
                        while (l < r && a[l] == a[l + 1]) l++;
                        while (l < r && a[r] == a[r - 1]) r--;
                        l++;
                        r--;
                    }
                }
            }
        }
        return out;
    }
}
