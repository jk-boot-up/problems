package com.jk.explore.problems.leetcode.p0503.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NextGreaterElementIITest {

    private final NextGreaterElementII solution = new NextGreaterElementII();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, -1, 2}, solution.nextGreaterElements(new int[]{1, 2, 1}));
        assertArrayEquals(new int[]{2, 3, 4, -1, 4}, solution.nextGreaterElements(new int[]{1, 2, 3, 4, 3}));
    }
}
