package com.jk.explore.problems.leetcode.p1291.v1;

import java.util.*;

public class SequentialDigits {

    public List<Integer> sequentialDigits(int low, int high) {
        String digits = "123456789";
        List<Integer> out = new ArrayList<>();
        for (int len = 2; len <= 9; len++)
            for (int start = 0; start + len <= 9; start++) {
                int v = Integer.parseInt(digits.substring(start, start + len));
                if (v >= low && v <= high) out.add(v);
            }
        return out;
    }
}
