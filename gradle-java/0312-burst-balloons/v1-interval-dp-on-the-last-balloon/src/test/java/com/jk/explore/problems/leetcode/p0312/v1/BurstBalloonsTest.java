package com.jk.explore.problems.leetcode.p0312.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BurstBalloonsTest {

    private final BurstBalloons solution = new BurstBalloons();

    @Test
    void examples() {
        assertEquals(167, solution.maxCoins(new int[]{3, 1, 5, 8}));
        assertEquals(10, solution.maxCoins(new int[]{1, 5}));
        assertEquals(7, solution.maxCoins(new int[]{7}));
    }
}
