package com.jk.explore.problems.leetcode.p1424.v1;

import java.util.*;

public class DiagonalTraverseII {

    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        List<List<Integer>> buckets = new ArrayList<>();
        int total = 0;
        for (int i = nums.size() - 1; i >= 0; i--) {
            List<Integer> row = nums.get(i);
            for (int j = 0; j < row.size(); j++) {
                while (buckets.size() <= i + j) buckets.add(new ArrayList<>());
                buckets.get(i + j).add(row.get(j));
                total++;
            }
        }
        int[] out = new int[total];
        int k = 0;
        for (List<Integer> b : buckets) for (int v : b) out[k++] = v;
        return out;
    }
}
