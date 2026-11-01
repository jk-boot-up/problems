package com.jk.explore.problems.leetcode.p0119.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PascalsTriangleIITest {

    private final PascalsTriangleII solution = new PascalsTriangleII();

    @Test
    void examples() {
        assertEquals(List.of(1, 3, 3, 1), solution.getRow(3));
        assertEquals(List.of(1), solution.getRow(0));
        assertEquals(List.of(1, 1), solution.getRow(1));
        assertEquals(1166803110, solution.getRow(33).get(16));
    }
}
