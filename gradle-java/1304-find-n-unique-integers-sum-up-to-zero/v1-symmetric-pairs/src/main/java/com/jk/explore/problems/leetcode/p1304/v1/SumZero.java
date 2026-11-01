package com.jk.explore.problems.leetcode.p1304.v1;

import java.util.*;

public class SumZero {

    public int[] sumZero(int n) {
        int[] out = new int[n];
        for (int k = 1, i = 0; k <= n / 2; k++) {
            out[i++] = k;
            out[i++] = -k;
        }
        return out;
    }
}
