package com.jk.explore.problems.leetcode.p0448.v1;

import java.util.*;

public class FindDisappearedNumbers {

    public List<Integer> findDisappearedNumbers(int[] nums) {
        int[] a = nums.clone();
        for (int x : a) {
            int i = Math.abs(x) - 1;
            if (a[i] > 0) a[i] = -a[i];
        }
        List<Integer> out = new ArrayList<>();
        for (int i = 0; i < a.length; i++) {
            if (a[i] > 0) out.add(i + 1);
        }
        return out;
    }
}
