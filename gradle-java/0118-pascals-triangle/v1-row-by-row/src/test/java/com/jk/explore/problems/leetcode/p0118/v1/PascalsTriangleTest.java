package com.jk.explore.problems.leetcode.p0118.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PascalsTriangleTest {

    private final PascalsTriangle solution = new PascalsTriangle();

    @Test
    void five() {
        assertEquals(List.of(List.of(1), List.of(1, 1), List.of(1, 2, 1), List.of(1, 3, 3, 1), List.of(1, 4, 6, 4, 1)), solution.generate(5));
    }

    @Test
    void one() {
        assertEquals(List.of(List.of(1)), solution.generate(1));
    }
}
