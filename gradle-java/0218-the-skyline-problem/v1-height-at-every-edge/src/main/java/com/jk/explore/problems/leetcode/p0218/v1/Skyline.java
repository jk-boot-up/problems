package com.jk.explore.problems.leetcode.p0218.v1;

import java.util.*;

public class Skyline {

    public List<List<Integer>> getSkyline(int[][] buildings) {
        int[] xs = new int[2 * buildings.length];
        for (int i = 0; i < buildings.length; i++) {
            xs[2 * i] = buildings[i][0];
            xs[2 * i + 1] = buildings[i][1];
        }
        Arrays.sort(xs);
        List<List<Integer>> out = new ArrayList<>();
        for (int k = 0; k < xs.length; k++) {
            int x = xs[k];
            if (k > 0 && x == xs[k - 1]) continue;
            int h = 0;
            for (int[] b : buildings) if (b[0] <= x && x < b[1]) h = Math.max(h, b[2]);
            if (out.isEmpty() || out.get(out.size() - 1).get(1) != h) out.add(List.of(x, h));
        }
        return out;
    }
}
