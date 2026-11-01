package com.jk.explore.problems.leetcode.p1260.v1;

import java.util.*;

public class Shift2DGrid {

    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length, total = m * n;
        Integer[] flat = new Integer[total];
        for (int i = 0; i < total; i++) flat[(i + k) % total] = grid[i / n][i % n];
        List<List<Integer>> out = new ArrayList<>();
        for (int r = 0; r < m; r++) out.add(new ArrayList<>(Arrays.asList(flat).subList(r * n, r * n + n)));
        return out;
    }
}
