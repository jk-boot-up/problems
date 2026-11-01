package com.jk.explore.problems.leetcode.p0650.v1;

import java.util.*;

public class TwoKeysKeyboard {

    public int minSteps(int n) {
        int[] best = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            best[i] = i;
            for (int d = 2; d < i; d++) if (i % d == 0) best[i] = Math.min(best[i], best[d] + i / d);
        }
        return best[n];
    }
}
