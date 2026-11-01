package com.jk.explore.problems.leetcode.p0179.v1;

import java.util.*;

public class LargestNumber {

    public String largestNumber(int[] nums) {
        String[] parts = new String[nums.length];
        for (int i = 0; i < nums.length; i++) parts[i] = String.valueOf(nums[i]);
        Arrays.sort(parts, (a, b) -> (b + a).compareTo(a + b));
        if (parts[0].equals("0")) return "0";
        return String.join("", parts);
    }
}
