package com.jk.explore.problems.leetcode.p0319.v1;

import java.util.*;

public class BulbSwitcher {

    public int bulbSwitch(int n) {
        int r = (int) Math.sqrt(n);
        while ((long) r * r > n) r--;
        while ((long) (r + 1) * (r + 1) <= n) r++;
        return r;
    }
}
