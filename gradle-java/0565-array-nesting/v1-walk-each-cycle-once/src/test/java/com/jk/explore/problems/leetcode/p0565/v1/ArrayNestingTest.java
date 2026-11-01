package com.jk.explore.problems.leetcode.p0565.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ArrayNestingTest {

    private final ArrayNesting solution = new ArrayNesting();

    @Test
    void examples() {
        assertEquals(4, solution.arrayNesting(new int[]{5, 4, 0, 3, 1, 6, 2}));
        assertEquals(1, solution.arrayNesting(new int[]{0, 1, 2}));
        assertEquals(3, solution.arrayNesting(new int[]{1, 2, 0}));
        assertEquals(2, solution.arrayNesting(new int[]{1, 0, 3, 2}));
    }
}
