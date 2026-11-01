package com.jk.explore.problems.leetcode.p0066.v1;

import java.util.*;

public class PlusOne {

    public int[] plusOne(int[] digits) {
        int[] d = digits.clone();
        for (int i = d.length - 1; i >= 0; i--) {
            if (d[i] < 9) {
                d[i]++;
                return d;
            }
            d[i] = 0;
        }
        int[] out = new int[d.length + 1];
        out[0] = 1;
        return out;
    }
}
