package com.jk.explore.problems.leetcode.p0118.v1;

import java.util.*;

public class PascalsTriangle {

    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> rows = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                row.add(j == 0 || j == i ? 1 : rows.get(i - 1).get(j - 1) + rows.get(i - 1).get(j));
            }
            rows.add(row);
        }
        return rows;
    }
}
