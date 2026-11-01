package com.jk.explore.problems.leetcode.p0502.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IPOTest {

    private final IPO solution = new IPO();

    @Test
    void example1() {
        assertEquals(4, solution.findMaximizedCapital(2, 0, new int[]{1, 2, 3}, new int[]{0, 1, 1}));
    }

    @Test
    void example2() {
        assertEquals(6, solution.findMaximizedCapital(3, 0, new int[]{1, 2, 3}, new int[]{0, 1, 2}));
    }

    @Test
    void cannotStart() {
        assertEquals(0, solution.findMaximizedCapital(1, 0, new int[]{1, 2, 3}, new int[]{1, 1, 2}));
    }
}
