package com.jk.explore.problems.leetcode.p0137.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SingleNumberIITest {

    private final SingleNumberII solution = new SingleNumberII();

    @Test
    void examples() {
        assertEquals(3, solution.singleNumber(new int[]{2, 2, 3, 2}));
        assertEquals(99, solution.singleNumber(new int[]{0, 1, 0, 1, 0, 1, 99}));
    }

    @Test
    void negative() {
        assertEquals(-4, solution.singleNumber(new int[]{-2, -2, 1, 1, -4, 1, -2}));
    }
}
