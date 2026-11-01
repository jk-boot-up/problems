package com.jk.explore.problems.leetcode.p0153.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindMinimumRotatedTest {

    private final FindMinimumRotated solution = new FindMinimumRotated();

    @Test
    void rotated() {
        assertEquals(1, solution.findMin(new int[]{3, 4, 5, 1, 2}));
        assertEquals(0, solution.findMin(new int[]{4, 5, 6, 7, 0, 1, 2}));
    }

    @Test
    void notRotated() {
        assertEquals(11, solution.findMin(new int[]{11, 13, 15, 17}));
    }

    @Test
    void single() {
        assertEquals(5, solution.findMin(new int[]{5}));
    }
}
