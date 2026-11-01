package com.jk.explore.problems.leetcode.p0309.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class StockWithCooldownTest {

    private final StockWithCooldown solution = new StockWithCooldown();

    @Test
    void examples() {
        assertEquals(3, solution.maxProfit(new int[]{1, 2, 3, 0, 2}));
        assertEquals(0, solution.maxProfit(new int[]{1}));
        assertEquals(3, solution.maxProfit(new int[]{2, 1, 4}));
    }
}
