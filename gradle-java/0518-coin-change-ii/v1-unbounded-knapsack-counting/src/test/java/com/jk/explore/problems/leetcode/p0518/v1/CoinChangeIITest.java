package com.jk.explore.problems.leetcode.p0518.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CoinChangeIITest {

    private final CoinChangeII solution = new CoinChangeII();

    @Test
    void examples() {
        assertEquals(4, solution.change(5, new int[]{1, 2, 5}));
        assertEquals(0, solution.change(3, new int[]{2}));
        assertEquals(1, solution.change(10, new int[]{10}));
        assertEquals(1, solution.change(0, new int[]{7}));
    }
}
