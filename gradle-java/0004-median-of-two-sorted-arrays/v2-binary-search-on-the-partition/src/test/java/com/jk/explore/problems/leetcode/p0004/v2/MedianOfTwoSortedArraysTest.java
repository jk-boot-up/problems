package com.jk.explore.problems.leetcode.p0004.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MedianOfTwoSortedArraysTest {

    private final MedianOfTwoSortedArrays solution = new MedianOfTwoSortedArrays();

    @Test
    void odd() {
        assertEquals(2.0, solution.findMedianSortedArrays(new int[]{1, 3}, new int[]{2}));
    }

    @Test
    void even() {
        assertEquals(2.5, solution.findMedianSortedArrays(new int[]{1, 2}, new int[]{3, 4}));
    }

    @Test
    void oneEmpty() {
        assertEquals(3.0, solution.findMedianSortedArrays(new int[]{}, new int[]{1, 3, 5}));
    }

    @Test
    void interleaved() {
        assertEquals(4.5, solution.findMedianSortedArrays(new int[]{1, 3, 5, 7}, new int[]{2, 4, 6, 8}));
    }
}
