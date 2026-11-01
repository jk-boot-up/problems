package com.jk.explore.problems.leetcode.p0977.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SquaresOfSortedArrayTest {

    private final SquaresOfSortedArray solution = new SquaresOfSortedArray();

    @Test
    void examples() {
        assertArrayEquals(new int[]{0, 1, 9, 16, 100}, solution.sortedSquares(new int[]{-4, -1, 0, 3, 10}));
        assertArrayEquals(new int[]{4, 9, 9, 49, 121}, solution.sortedSquares(new int[]{-7, -3, 2, 3, 11}));
    }
}
