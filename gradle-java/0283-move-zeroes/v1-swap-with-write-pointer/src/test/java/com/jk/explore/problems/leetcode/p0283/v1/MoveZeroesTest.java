package com.jk.explore.problems.leetcode.p0283.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MoveZeroesTest {

    private final MoveZeroes solution = new MoveZeroes();

    @Test
    void example() {
        int[] a = {0, 1, 0, 3, 12};
        solution.moveZeroes(a);
        assertArrayEquals(new int[]{1, 3, 12, 0, 0}, a);
    }

    @Test
    void noZeros() {
        int[] a = {1, 2};
        solution.moveZeroes(a);
        assertArrayEquals(new int[]{1, 2}, a);
    }
}
