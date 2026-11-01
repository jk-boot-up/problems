package com.jk.explore.problems.leetcode.p0069.v2;

import java.util.*;

public class SqrtX {

    public int mySqrt(int x) {
        long r = x;
        while (r * r > x) {
            r = (r + x / r) / 2;
        }
        return (int) r;
    }
}
