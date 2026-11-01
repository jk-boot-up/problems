package com.jk.explore.problems.leetcode.p0386.v1;

import java.util.*;

public class LexicographicalNumbers {

    public List<Integer> lexicalOrder(int n) {
        List<Integer> out = new ArrayList<>(n);
        int cur = 1;
        for (int i = 0; i < n; i++) {
            out.add(cur);
            if (cur * 10 <= n) cur *= 10;
            else {
                while (cur % 10 == 9 || cur + 1 > n) cur /= 10;
                cur++;
            }
        }
        return out;
    }
}
