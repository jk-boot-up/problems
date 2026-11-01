package com.jk.explore.problems.leetcode.p0673.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NumberOfLISTest {

    private final NumberOfLIS solution = new NumberOfLIS();

    @Test
    void examples() {
        assertEquals(2, solution.findNumberOfLIS(new int[]{1, 3, 5, 4, 7}));
        assertEquals(5, solution.findNumberOfLIS(new int[]{2, 2, 2, 2, 2}));
        assertEquals(3, solution.findNumberOfLIS(new int[]{1, 2, 4, 3, 5, 4, 7, 2}));
        assertEquals(1, solution.findNumberOfLIS(new int[]{7}));
    }
}
