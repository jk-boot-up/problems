package com.jk.explore.problems.leetcode.p0485.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaxConsecutiveOnesTest {

    private final MaxConsecutiveOnes solution = new MaxConsecutiveOnes();

    @Test
    void examples() {
        assertEquals(3, solution.findMaxConsecutiveOnes(new int[]{1, 1, 0, 1, 1, 1}));
        assertEquals(2, solution.findMaxConsecutiveOnes(new int[]{1, 0, 1, 1, 0, 1}));
        assertEquals(0, solution.findMaxConsecutiveOnes(new int[]{0}));
    }
}
