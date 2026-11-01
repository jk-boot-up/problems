package com.jk.explore.problems.leetcode.p0031.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NextPermutationTest {

    private final NextPermutation solution = new NextPermutation();

    private int[] next(int... a) {
        solution.nextPermutation(a);
        return a;
    }

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 3, 2}, next(1, 2, 3));
        assertArrayEquals(new int[]{1, 2, 3}, next(3, 2, 1));
        assertArrayEquals(new int[]{1, 5, 1}, next(1, 1, 5));
    }

    @Test
    void middle() {
        assertArrayEquals(new int[]{1, 3, 1, 2}, next(1, 2, 3, 1));
    }
}
