package com.jk.explore.problems.leetcode.p0223.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RectangleAreaTest {

    private final RectangleArea solution = new RectangleArea();

    @Test
    void examples() {
        assertEquals(45, solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2));
        assertEquals(16, solution.computeArea(-2, -2, 2, 2, -2, -2, 2, 2));
        assertEquals(2, solution.computeArea(0, 0, 1, 1, 2, 2, 3, 3));
        assertEquals(2, solution.computeArea(0, 0, 1, 1, 1, 0, 2, 1));
    }
}
