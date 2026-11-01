package com.jk.explore.problems.leetcode.p0376.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class WiggleSubsequenceTest {

    private final WiggleSubsequence solution = new WiggleSubsequence();

    @Test
    void examples() {
        assertEquals(6, solution.wiggleMaxLength(new int[]{1, 7, 4, 9, 2, 5}));
        assertEquals(7, solution.wiggleMaxLength(new int[]{1, 17, 5, 10, 13, 15, 10, 5, 16, 8}));
        assertEquals(2, solution.wiggleMaxLength(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9}));
        assertEquals(1, solution.wiggleMaxLength(new int[]{0, 0}));
        assertEquals(1, solution.wiggleMaxLength(new int[]{5}));
        assertEquals(3, solution.wiggleMaxLength(new int[]{3, 3, 3, 2, 5}));
    }
}
