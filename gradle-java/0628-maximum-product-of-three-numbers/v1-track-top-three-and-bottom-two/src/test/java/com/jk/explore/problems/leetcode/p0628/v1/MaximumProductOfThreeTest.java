package com.jk.explore.problems.leetcode.p0628.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumProductOfThreeTest {

    private final MaximumProductOfThree solution = new MaximumProductOfThree();

    @Test
    void examples() {
        assertEquals(6, solution.maximumProduct(new int[]{1, 2, 3}));
        assertEquals(24, solution.maximumProduct(new int[]{1, 2, 3, 4}));
        assertEquals(-6, solution.maximumProduct(new int[]{-1, -2, -3}));
        assertEquals(300, solution.maximumProduct(new int[]{-10, -10, 1, 3, 2}));
    }
}
