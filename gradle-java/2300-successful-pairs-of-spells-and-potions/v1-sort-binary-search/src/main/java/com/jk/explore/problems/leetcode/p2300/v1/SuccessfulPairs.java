package com.jk.explore.problems.leetcode.p2300.v1;

import java.util.*;

public class SuccessfulPairs {

    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int[] p = potions.clone();
        Arrays.sort(p);
        int[] out = new int[spells.length];
        for (int i = 0; i < spells.length; i++) {
            long need = (success + spells[i] - 1) / spells[i];
            int lo = 0, hi = p.length;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (p[mid] < need) lo = mid + 1; else hi = mid;
            }
            out[i] = p.length - lo;
        }
        return out;
    }
}
