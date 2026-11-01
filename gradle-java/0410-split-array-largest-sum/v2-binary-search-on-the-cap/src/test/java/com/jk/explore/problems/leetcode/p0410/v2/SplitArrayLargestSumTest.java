package com.jk.explore.problems.leetcode.p0410.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SplitArrayLargestSumTest {

    private final SplitArrayLargestSum solution = new SplitArrayLargestSum();

    @Test
    void examples() {
        assertEquals(18, solution.splitArray(new int[]{7, 2, 5, 10, 8}, 2));
        assertEquals(9, solution.splitArray(new int[]{1, 2, 3, 4, 5}, 2));
        assertEquals(4, solution.splitArray(new int[]{1, 4, 4}, 3));
        assertEquals(0, solution.splitArray(new int[]{0}, 1));
        assertEquals(32, solution.splitArray(new int[]{7, 2, 5, 10, 8}, 1));
        assertEquals(10, solution.splitArray(new int[]{7, 2, 5, 10, 8}, 5));
    }
}
