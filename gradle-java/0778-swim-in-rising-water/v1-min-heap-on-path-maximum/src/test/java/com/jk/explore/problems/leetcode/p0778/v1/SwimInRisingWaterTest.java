package com.jk.explore.problems.leetcode.p0778.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SwimInRisingWaterTest {

    private final SwimInRisingWater solution = new SwimInRisingWater();

    @Test
    void examples() {
        assertEquals(3, solution.swimInWater(new int[][]{{0, 2}, {1, 3}}));
        assertEquals(16, solution.swimInWater(new int[][]{{0, 1, 2, 3, 4}, {24, 23, 22, 21, 5}, {12, 13, 14, 15, 16}, {11, 17, 18, 19, 20}, {10, 9, 8, 7, 6}}));
    }
}
