package com.jk.explore.problems.leetcode.p0057.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class InsertIntervalTest {

    private final InsertInterval solution = new InsertInterval();

    @Test
    void example1() {
        assertArrayEquals(new int[][]{{1, 5}, {6, 9}}, solution.insert(new int[][]{{1, 3}, {6, 9}}, new int[]{2, 5}));
    }

    @Test
    void mergesSeveral() {
        assertArrayEquals(new int[][]{{1, 2}, {3, 10}, {12, 16}},
                solution.insert(new int[][]{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}}, new int[]{4, 8}));
    }

    @Test
    void intoEmpty() {
        assertArrayEquals(new int[][]{{5, 7}}, solution.insert(new int[][]{}, new int[]{5, 7}));
    }
}
