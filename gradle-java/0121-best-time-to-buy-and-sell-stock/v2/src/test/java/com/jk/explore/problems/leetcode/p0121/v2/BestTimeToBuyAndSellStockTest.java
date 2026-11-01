package com.jk.explore.problems.leetcode.p0121.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BestTimeToBuyAndSellStockTest {

    private final BestTimeToBuyAndSellStock solution = new BestTimeToBuyAndSellStock();

    @Test
    void example1() {
        assertEquals(5, solution.maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
    }

    @Test
    void decreasingPrices() {
        assertEquals(0, solution.maxProfit(new int[]{7, 6, 4, 3, 1}));
    }

    @Test
    void singleDay() {
        assertEquals(0, solution.maxProfit(new int[]{3}));
    }
}
