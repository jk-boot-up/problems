package com.jk.explore.problems.leetcode.p0378.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KthSmallestInMatrixTest {

    private final KthSmallestInMatrix solution = new KthSmallestInMatrix();

    @Test
    void examples() {
        assertEquals(13, solution.kthSmallest(new int[][]{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}}, 8));
        assertEquals(-5, solution.kthSmallest(new int[][]{{-5}}, 1));
        assertEquals(1, solution.kthSmallest(new int[][]{{1, 2}, {1, 3}}, 2));
        assertEquals(1, solution.kthSmallest(new int[][]{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}}, 1));
        assertEquals(15, solution.kthSmallest(new int[][]{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}}, 9));
    }

    @Test
    void extremes() {
        assertEquals(-1_000_000_000, solution.kthSmallest(new int[][]{{-1_000_000_000, 1_000_000_000}, {1_000_000_000, 1_000_000_000}}, 1));
        assertEquals(1_000_000_000, solution.kthSmallest(new int[][]{{-1_000_000_000, 1_000_000_000}, {1_000_000_000, 1_000_000_000}}, 2));
    }
}
