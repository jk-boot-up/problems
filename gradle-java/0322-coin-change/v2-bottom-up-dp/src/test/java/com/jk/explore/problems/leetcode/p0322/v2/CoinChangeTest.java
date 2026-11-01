package com.jk.explore.problems.leetcode.p0322.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CoinChangeTest {

    private final CoinChange solution = new CoinChange();

    @Test
    void examples() {
        assertEquals(3, solution.coinChange(new int[]{1, 2, 5}, 11));
        assertEquals(-1, solution.coinChange(new int[]{2}, 3));
        assertEquals(0, solution.coinChange(new int[]{1}, 0));
    }

    @Test
    void greedyFails() {
        assertEquals(2, solution.coinChange(new int[]{1, 3, 4}, 6));
    }

    @Test
    void hugeCoin() {
        assertEquals(1, solution.coinChange(new int[]{2147483647, 1}, 1));
    }
}
