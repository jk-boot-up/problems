package com.jk.explore.problems.leetcode.p1658.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinOperationsReduceXTest {

    private final MinOperationsReduceX solution = new MinOperationsReduceX();

    @Test
    void examples() {
        assertEquals(2, solution.minOperations(new int[]{1, 1, 4, 2, 3}, 5));
        assertEquals(-1, solution.minOperations(new int[]{5, 6, 7, 8, 9}, 4));
        assertEquals(5, solution.minOperations(new int[]{3, 2, 20, 1, 1, 3}, 10));
        assertEquals(-1, solution.minOperations(new int[]{1, 1}, 3));
        assertEquals(1, solution.minOperations(new int[]{5}, 5));
        assertEquals(3, solution.minOperations(new int[]{1, 2, 3}, 6));
    }
}
