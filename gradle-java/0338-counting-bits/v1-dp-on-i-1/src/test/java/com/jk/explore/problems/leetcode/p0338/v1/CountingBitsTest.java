package com.jk.explore.problems.leetcode.p0338.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CountingBitsTest {

    private final CountingBits solution = new CountingBits();

    @Test
    void examples() {
        assertArrayEquals(new int[]{0, 1, 1}, solution.countBits(2));
        assertArrayEquals(new int[]{0, 1, 1, 2, 1, 2}, solution.countBits(5));
        assertArrayEquals(new int[]{0}, solution.countBits(0));
    }
}
