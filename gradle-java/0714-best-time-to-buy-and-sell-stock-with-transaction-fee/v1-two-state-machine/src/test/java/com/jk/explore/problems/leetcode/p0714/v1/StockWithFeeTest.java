package com.jk.explore.problems.leetcode.p0714.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class StockWithFeeTest {

    private final StockWithFee solution = new StockWithFee();

    @Test
    void examples() {
        assertEquals(8, solution.maxProfit(new int[]{1, 3, 2, 8, 4, 9}, 2));
        assertEquals(6, solution.maxProfit(new int[]{1, 3, 7, 5, 10, 3}, 3));
    }
}
