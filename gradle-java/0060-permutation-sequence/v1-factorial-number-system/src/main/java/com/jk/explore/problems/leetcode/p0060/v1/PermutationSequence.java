package com.jk.explore.problems.leetcode.p0060.v1;

import java.util.*;

public class PermutationSequence {

    public String getPermutation(int n, int k) {
        List<Integer> digits = new ArrayList<>();
        int[] fact = new int[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            digits.add(i);
            fact[i] = fact[i - 1] * i;
        }
        StringBuilder sb = new StringBuilder();
        k--;
        for (int m = n; m >= 1; m--) {
            int block = k / fact[m - 1];
            sb.append(digits.remove(block));
            k %= fact[m - 1];
        }
        return sb.toString();
    }
}
