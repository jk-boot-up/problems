package com.jk.explore.problems.leetcode.p0221.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximalSquareTest {

    private final MaximalSquare solution = new MaximalSquare();

    private static char[][] m(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void example() {
        assertEquals(4, solution.maximalSquare(m("10100", "10111", "11111", "10010")));
    }

    @Test
    void small() {
        assertEquals(1, solution.maximalSquare(m("01", "10")));
        assertEquals(0, solution.maximalSquare(m("0")));
    }

    @Test
    void full() {
        assertEquals(9, solution.maximalSquare(m("111", "111", "111")));
    }
}
