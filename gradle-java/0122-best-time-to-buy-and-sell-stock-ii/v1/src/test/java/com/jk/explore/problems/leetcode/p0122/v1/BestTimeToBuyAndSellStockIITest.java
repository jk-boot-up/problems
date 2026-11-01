package com.jk.explore.problems.leetcode.p0122.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BestTimeToBuyAndSellStockIITest {

    private final BestTimeToBuyAndSellStockII solution = new BestTimeToBuyAndSellStockII();

    @Test
    void example1() {
        assertEquals(7, solution.maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
    }

    @Test
    void increasing() {
        assertEquals(4, solution.maxProfit(new int[]{1, 2, 3, 4, 5}));
    }

    @Test
    void decreasing() {
        assertEquals(0, solution.maxProfit(new int[]{7, 6, 4, 3, 1}));
    }
}
