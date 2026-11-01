package com.jk.explore.problems.leetcode.p0089.v1;

import java.util.*;

public class GrayCode {

    public List<Integer> grayCode(int n) {
        List<Integer> out = new ArrayList<>();
        for (int i = 0; i < (1 << n); i++) out.add(i ^ (i >> 1));
        return out;
    }
}
