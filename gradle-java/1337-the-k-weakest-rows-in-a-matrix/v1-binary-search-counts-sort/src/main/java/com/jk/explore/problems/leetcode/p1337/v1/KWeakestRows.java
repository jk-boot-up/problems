package com.jk.explore.problems.leetcode.p1337.v1;

import java.util.*;

public class KWeakestRows {

    public int[] kWeakestRows(int[][] mat, int k) {
        int m = mat.length;
        int[] key = new int[m];
        for (int i = 0; i < m; i++) key[i] = soldiers(mat[i]) * m + i;
        Arrays.sort(key);
        int[] out = new int[k];
        for (int i = 0; i < k; i++) out[i] = key[i] % m;
        return out;
    }

    private int soldiers(int[] row) {
        int lo = 0, hi = row.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (row[mid] == 1) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
