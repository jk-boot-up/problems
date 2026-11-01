package com.jk.explore.problems.leetcode.p0018.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FourSumTest {

    private final FourSum solution = new FourSum();

    @Test
    void examples() {
        assertEquals(List.of(List.of(-2, -1, 1, 2), List.of(-2, 0, 0, 2), List.of(-1, 0, 0, 1)), solution.fourSum(new int[]{1, 0, -1, 0, -2, 2}, 0));
        assertEquals(List.of(List.of(2, 2, 2, 2)), solution.fourSum(new int[]{2, 2, 2, 2, 2}, 8));
    }

    @Test
    void overflow() {
        assertEquals(List.of(), solution.fourSum(new int[]{1000000000, 1000000000, 1000000000, 1000000000}, -294967296));
    }
}
