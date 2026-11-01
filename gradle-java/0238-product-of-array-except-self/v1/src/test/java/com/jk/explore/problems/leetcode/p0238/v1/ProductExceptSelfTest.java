package com.jk.explore.problems.leetcode.p0238.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ProductExceptSelfTest {

    private final ProductExceptSelf solution = new ProductExceptSelf();

    @Test
    void example1() {
        assertArrayEquals(new int[]{24, 12, 8, 6}, solution.productExceptSelf(new int[]{1, 2, 3, 4}));
    }

    @Test
    void withZero() {
        assertArrayEquals(new int[]{0, 0, 9, 0, 0}, solution.productExceptSelf(new int[]{-1, 1, 0, -3, 3}));
    }

    @Test
    void twoElements() {
        assertArrayEquals(new int[]{3, 2}, solution.productExceptSelf(new int[]{2, 3}));
    }
}
