package com.jk.explore.problems.leetcode.p2352.v1;

import java.util.*;

public class EqualRowColumnPairs {

    public int equalPairs(int[][] grid) {
        int n = grid.length, pairs = 0;
        MyHashMap<List<Integer>, Integer> rows = new MyHashMap<>();
        for (int[] row : grid) {
            List<Integer> key = new ArrayList<>();
            for (int v : row) key.add(v);
            rows.merge(key, 1, Integer::sum);
        }
        for (int c = 0; c < n; c++) {
            List<Integer> key = new ArrayList<>();
            for (int r = 0; r < n; r++) key.add(grid[r][c]);
            pairs += rows.getOrDefault(key, 0);
        }
        return pairs;
    }
}
