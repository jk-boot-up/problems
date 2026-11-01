package com.jk.explore.problems.leetcode.p0496.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NextGreaterElementITest {

    private final NextGreaterElementI solution = new NextGreaterElementI();

    @Test
    void examples() {
        assertArrayEquals(new int[]{-1, 3, -1}, solution.nextGreaterElement(new int[]{4, 1, 2}, new int[]{1, 3, 4, 2}));
        assertArrayEquals(new int[]{3, -1}, solution.nextGreaterElement(new int[]{2, 4}, new int[]{1, 2, 3, 4}));
    }
}
