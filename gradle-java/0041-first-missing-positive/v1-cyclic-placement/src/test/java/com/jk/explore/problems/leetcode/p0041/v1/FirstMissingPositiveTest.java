package com.jk.explore.problems.leetcode.p0041.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FirstMissingPositiveTest {

    private final FirstMissingPositive solution = new FirstMissingPositive();

    @Test
    void examples() {
        assertEquals(3, solution.firstMissingPositive(new int[]{1, 2, 0}));
        assertEquals(2, solution.firstMissingPositive(new int[]{3, 4, -1, 1}));
        assertEquals(1, solution.firstMissingPositive(new int[]{7, 8, 9, 11, 12}));
    }

    @Test
    void duplicatesAndFull() {
        assertEquals(2, solution.firstMissingPositive(new int[]{1, 1}));
        assertEquals(4, solution.firstMissingPositive(new int[]{3, 1, 2}));
    }
}
