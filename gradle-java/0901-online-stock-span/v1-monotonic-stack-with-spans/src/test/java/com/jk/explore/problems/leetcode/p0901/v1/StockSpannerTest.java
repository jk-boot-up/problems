package com.jk.explore.problems.leetcode.p0901.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class StockSpannerTest {

    @Test
    void example() {
        StockSpanner s = new StockSpanner();
        int[] prices = {100, 80, 60, 70, 60, 75, 85};
        int[] spans = {1, 1, 1, 2, 1, 4, 6};
        for (int i = 0; i < prices.length; i++) assertEquals(spans[i], s.next(prices[i]));
    }
}
