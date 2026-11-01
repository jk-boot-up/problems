package com.jk.explore.problems.leetcode.p1475.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FinalPricesTest {

    private final FinalPrices solution = new FinalPrices();

    @Test
    void examples() {
        assertArrayEquals(new int[]{4, 2, 4, 2, 3}, solution.finalPrices(new int[]{8, 4, 6, 2, 3}));
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, solution.finalPrices(new int[]{1, 2, 3, 4, 5}));
        assertArrayEquals(new int[]{9, 0, 1, 6}, solution.finalPrices(new int[]{10, 1, 1, 6}));
    }
}
