package com.jk.explore.problems.leetcode.p0650.v2;

import java.util.*;

public class TwoKeysKeyboard {

    public int minSteps(int n) {
        int steps = 0;
        for (int d = 2; d * d <= n; d++)
            while (n % d == 0) {
                steps += d;
                n /= d;
            }
        if (n > 1) steps += n;
        return steps;
    }
}
