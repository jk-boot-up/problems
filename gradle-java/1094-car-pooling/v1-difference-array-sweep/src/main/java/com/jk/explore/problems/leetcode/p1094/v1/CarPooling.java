package com.jk.explore.problems.leetcode.p1094.v1;

import java.util.*;

public class CarPooling {

    public boolean carPooling(int[][] trips, int capacity) {
        int[] change = new int[1001];
        for (int[] t : trips) {
            change[t[1]] += t[0];
            change[t[2]] -= t[0];
        }
        int load = 0;
        for (int c : change) if ((load += c) > capacity) return false;
        return true;
    }
}
