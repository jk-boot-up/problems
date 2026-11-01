package com.jk.explore.problems.leetcode.p0154.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindMinimumRotatedIITest {

    private final FindMinimumRotatedII solution = new FindMinimumRotatedII();

    @Test
    void examples() {
        assertEquals(1, solution.findMin(new int[]{1, 3, 5}));
        assertEquals(0, solution.findMin(new int[]{2, 2, 2, 0, 1}));
        assertEquals(1, solution.findMin(new int[]{3, 1, 3}));
        assertEquals(1, solution.findMin(new int[]{1, 1, 1, 1}));
    }
}
