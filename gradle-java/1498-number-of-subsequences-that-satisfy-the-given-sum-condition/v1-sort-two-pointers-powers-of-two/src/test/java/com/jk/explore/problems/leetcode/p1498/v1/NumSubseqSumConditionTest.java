package com.jk.explore.problems.leetcode.p1498.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NumSubseqSumConditionTest {

    private final NumSubseqSumCondition solution = new NumSubseqSumCondition();

    @Test
    void examples() {
        assertEquals(4, solution.numSubseq(new int[]{3, 5, 6, 7}, 9));
        assertEquals(6, solution.numSubseq(new int[]{3, 3, 6, 8}, 10));
        assertEquals(61, solution.numSubseq(new int[]{2, 3, 3, 4, 6, 7}, 12));
        assertEquals(0, solution.numSubseq(new int[]{5}, 9));
    }

    @Test
    void largeIsReducedModulo() {
        int[] ones = new int[100];
        Arrays.fill(ones, 1);
        long expected = 1;
        for (int i = 0; i < 100; i++) expected = expected * 2 % 1_000_000_007;
        assertEquals((expected - 1 + 1_000_000_007) % 1_000_000_007, solution.numSubseq(ones, 2));
    }
}
