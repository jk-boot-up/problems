package com.jk.explore.problems.leetcode.p0123.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BestTimeToBuyAndSellStockIIITest {

    private final BestTimeToBuyAndSellStockIII solution = new BestTimeToBuyAndSellStockIII();

    @Test
    void twoTrades() {
        assertEquals(6, solution.maxProfit(new int[]{3, 3, 5, 0, 0, 3, 1, 4}));
    }

    @Test
    void oneTradeEnough() {
        assertEquals(4, solution.maxProfit(new int[]{1, 2, 3, 4, 5}));
    }

    @Test
    void none() {
        assertEquals(0, solution.maxProfit(new int[]{7, 6, 4, 3, 1}));
        assertEquals(0, solution.maxProfit(new int[]{1}));
    }
}
