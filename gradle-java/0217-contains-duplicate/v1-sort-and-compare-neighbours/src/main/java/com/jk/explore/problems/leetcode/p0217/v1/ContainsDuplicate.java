package com.jk.explore.problems.leetcode.p0217.v1;

import java.util.*;

public class ContainsDuplicate {

    public boolean containsDuplicate(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        for (int i = 1; i < a.length; i++) {
            if (a[i] == a[i - 1]) return true;
        }
        return false;
    }
}
