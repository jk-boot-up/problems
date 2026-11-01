package com.jk.explore.problems.leetcode.p0260.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SingleNumberIIITest {

    private final SingleNumberIII solution = new SingleNumberIII();

    private int[] sorted(int[] a) {
        Arrays.sort(a);
        return a;
    }

    @Test
    void examples() {
        assertArrayEquals(new int[]{3, 5}, sorted(solution.singleNumber(new int[]{1, 2, 1, 3, 2, 5})));
        assertArrayEquals(new int[]{-1, 0}, sorted(solution.singleNumber(new int[]{-1, 0})));
        assertArrayEquals(new int[]{0, 1}, sorted(solution.singleNumber(new int[]{0, 1})));
        assertArrayEquals(new int[]{Integer.MIN_VALUE, 7}, sorted(solution.singleNumber(new int[]{7, 4, Integer.MIN_VALUE, 4})));
    }
}
