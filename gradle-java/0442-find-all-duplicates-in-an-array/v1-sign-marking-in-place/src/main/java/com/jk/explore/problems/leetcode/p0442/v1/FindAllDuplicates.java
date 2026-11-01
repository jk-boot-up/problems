package com.jk.explore.problems.leetcode.p0442.v1;

import java.util.*;

public class FindAllDuplicates {

    public List<Integer> findDuplicates(int[] nums) {
        int[] a = nums.clone();
        List<Integer> out = new ArrayList<>();
        for (int x : a) {
            int i = Math.abs(x) - 1;
            if (a[i] < 0) out.add(i + 1);
            else a[i] = -a[i];
        }
        return out;
    }
}
