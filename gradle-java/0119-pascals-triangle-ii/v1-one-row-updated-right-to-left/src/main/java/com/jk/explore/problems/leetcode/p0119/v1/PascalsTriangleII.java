package com.jk.explore.problems.leetcode.p0119.v1;

import java.util.*;

public class PascalsTriangleII {

    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>(List.of(1));
        for (int i = 1; i <= rowIndex; i++) {
            row.add(1);
            for (int j = i - 1; j >= 1; j--) row.set(j, row.get(j) + row.get(j - 1));
        }
        return row;
    }
}
