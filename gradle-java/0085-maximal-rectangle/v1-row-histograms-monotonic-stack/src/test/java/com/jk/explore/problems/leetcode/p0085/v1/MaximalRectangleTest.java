package com.jk.explore.problems.leetcode.p0085.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximalRectangleTest {

    private final MaximalRectangle solution = new MaximalRectangle();

    private static char[][] m(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void example() {
        assertEquals(6, solution.maximalRectangle(m("10100", "10111", "11111", "10010")));
    }

    @Test
    void small() {
        assertEquals(0, solution.maximalRectangle(m("0")));
        assertEquals(1, solution.maximalRectangle(m("1")));
    }
}
