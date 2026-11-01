package com.jk.explore.problems.leetcode.p0581.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ShortestUnsortedSubarrayTest {

    private final ShortestUnsortedSubarray solution = new ShortestUnsortedSubarray();

    @Test
    void examples() {
        assertEquals(5, solution.findUnsortedSubarray(new int[]{2, 6, 4, 8, 10, 9, 15}));
        assertEquals(0, solution.findUnsortedSubarray(new int[]{1, 2, 3, 4}));
        assertEquals(0, solution.findUnsortedSubarray(new int[]{1}));
        assertEquals(4, solution.findUnsortedSubarray(new int[]{1, 3, 2, 2, 2}));
        assertEquals(2, solution.findUnsortedSubarray(new int[]{2, 1}));
        assertEquals(0, solution.findUnsortedSubarray(new int[]{2, 2, 2}));
    }
}
