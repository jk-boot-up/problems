package com.jk.explore.problems.leetcode.p0015.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ThreeSumTest {

    private final ThreeSum solution = new ThreeSum();

    @Test
    void example1() {
        assertEquals(Set.of(List.of(-1, -1, 2), List.of(-1, 0, 1)), new HashSet<>(solution.threeSum(new int[]{-1, 0, 1, 2, -1, -4})));
    }

    @Test
    void none() {
        assertEquals(List.of(), solution.threeSum(new int[]{0, 1, 1}));
    }

    @Test
    void zeros() {
        assertEquals(List.of(List.of(0, 0, 0)), solution.threeSum(new int[]{0, 0, 0, 0}));
    }
}
