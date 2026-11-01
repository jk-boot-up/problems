package com.jk.explore.problems.leetcode.p1588.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SumOddLengthSubarraysTest {

    private final SumOddLengthSubarrays solution = new SumOddLengthSubarrays();

    @Test
    void examples() {
        assertEquals(58, solution.sumOddLengthSubarrays(new int[]{1, 4, 2, 5, 3}));
        assertEquals(3, solution.sumOddLengthSubarrays(new int[]{1, 2}));
        assertEquals(66, solution.sumOddLengthSubarrays(new int[]{10, 11, 12}));
        assertEquals(7, solution.sumOddLengthSubarrays(new int[]{7}));
    }
}
