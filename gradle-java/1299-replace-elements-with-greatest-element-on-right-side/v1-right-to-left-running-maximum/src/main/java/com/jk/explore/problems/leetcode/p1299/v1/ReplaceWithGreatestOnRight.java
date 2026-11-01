package com.jk.explore.problems.leetcode.p1299.v1;

import java.util.*;

public class ReplaceWithGreatestOnRight {

    public int[] replaceElements(int[] arr) {
        int[] out = new int[arr.length];
        int max = -1;
        for (int i = arr.length - 1; i >= 0; i--) {
            out[i] = max;
            max = Math.max(max, arr[i]);
        }
        return out;
    }
}
