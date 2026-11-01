package com.jk.explore.problems.leetcode.p0056.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MergeIntervalsTest {

    private final MergeIntervals solution = new MergeIntervals();

    @Test
    void example1() {
        assertArrayEquals(new int[][]{{1, 6}, {8, 10}, {15, 18}}, solution.merge(new int[][]{{1, 3}, {2, 6}, {8, 10}, {15, 18}}));
    }

    @Test
    void touching() {
        assertArrayEquals(new int[][]{{1, 5}}, solution.merge(new int[][]{{1, 4}, {4, 5}}));
    }

    @Test
    void unsortedAndNested() {
        assertArrayEquals(new int[][]{{0, 5}}, solution.merge(new int[][]{{2, 3}, {0, 5}, {1, 4}}));
    }
}
