package com.jk.explore.problems.leetcode.p0202.v1;

import java.util.*;

public class HappyNumber {

    private static int next(int x) {
        int sum = 0;
        while (x > 0) {
            int d = x % 10;
            sum += d * d;
            x /= 10;
        }
        return sum;
    }

    public boolean isHappy(int n) {
        MyHashSet<Integer> seen = new MyHashSet<>();
        while (n != 1 && seen.add(n)) {
            n = next(n);
        }
        return n == 1;
    }
}
