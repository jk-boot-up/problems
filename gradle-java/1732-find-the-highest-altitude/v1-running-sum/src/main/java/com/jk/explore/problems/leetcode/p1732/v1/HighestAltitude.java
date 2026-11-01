package com.jk.explore.problems.leetcode.p1732.v1;

import java.util.*;

public class HighestAltitude {

    public int largestAltitude(int[] gain) {
        int altitude = 0, best = 0;
        for (int g : gain) {
            altitude += g;
            best = Math.max(best, altitude);
        }
        return best;
    }
}
