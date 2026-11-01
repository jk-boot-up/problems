package com.jk.explore.problems.leetcode.p0120.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TriangleTest {

    private final Triangle solution = new Triangle();

    @Test
    void example() {
        assertEquals(11, solution.minimumTotal(List.of(List.of(2), List.of(3, 4), List.of(6, 5, 7), List.of(4, 1, 8, 3))));
    }

    @Test
    void single() {
        assertEquals(-10, solution.minimumTotal(List.of(List.of(-10))));
    }
}
