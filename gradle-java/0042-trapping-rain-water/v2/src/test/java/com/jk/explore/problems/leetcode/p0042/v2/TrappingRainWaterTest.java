package com.jk.explore.problems.leetcode.p0042.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TrappingRainWaterTest {

    private final TrappingRainWater solution = new TrappingRainWater();

    @Test
    void example1() {
        assertEquals(6, solution.trap(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}));
    }

    @Test
    void example2() {
        assertEquals(9, solution.trap(new int[]{4, 2, 0, 3, 2, 5}));
    }

    @Test
    void noWalls() {
        assertEquals(0, solution.trap(new int[]{1, 2, 3}));
    }
}
