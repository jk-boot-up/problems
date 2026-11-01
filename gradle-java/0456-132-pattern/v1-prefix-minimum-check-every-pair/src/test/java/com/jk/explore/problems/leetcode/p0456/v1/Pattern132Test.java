package com.jk.explore.problems.leetcode.p0456.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class Pattern132Test {

    private final Pattern132 solution = new Pattern132();

    @Test
    void examples() {
        assertFalse(solution.find132pattern(new int[]{1, 2, 3, 4}));
        assertTrue(solution.find132pattern(new int[]{3, 1, 4, 2}));
        assertTrue(solution.find132pattern(new int[]{-1, 3, 2, 0}));
        assertFalse(solution.find132pattern(new int[]{1, 0, 1, -4, -3}));
        assertTrue(solution.find132pattern(new int[]{3, 5, 0, 3, 4}));
        assertFalse(solution.find132pattern(new int[]{1}));
        assertFalse(solution.find132pattern(new int[]{Integer.MIN_VALUE, Integer.MIN_VALUE}));
    }
}
