package com.jk.explore.problems.leetcode.p0188.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BestTimeToBuyAndSellStockIVTest {

    private final BestTimeToBuyAndSellStockIV solution = new BestTimeToBuyAndSellStockIV();

    @Test
    void examples() {
        assertEquals(2, solution.maxProfit(2, new int[]{2, 4, 1}));
        assertEquals(7, solution.maxProfit(2, new int[]{3, 2, 6, 5, 0, 3}));
    }

    @Test
    void limitBinds() {
        assertEquals(6, solution.maxProfit(1, new int[]{1, 3, 1, 7}));
        assertEquals(8, solution.maxProfit(2, new int[]{1, 3, 1, 7}));
    }

    @Test
    void largeK() {
        assertEquals(8, solution.maxProfit(100, new int[]{1, 3, 1, 7}));
    }
}
