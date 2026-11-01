package com.jk.explore.problems.leetcode.p0525.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ContiguousArrayTest {

    private final ContiguousArray solution = new ContiguousArray();

    @Test
    void examples() {
        assertEquals(2, solution.findMaxLength(new int[]{0, 1}));
        assertEquals(2, solution.findMaxLength(new int[]{0, 1, 0}));
        assertEquals(6, solution.findMaxLength(new int[]{0, 1, 1, 1, 1, 1, 0, 0, 0}));
        assertEquals(6, solution.findMaxLength(new int[]{0, 0, 1, 0, 0, 0, 1, 1}));
        assertEquals(0, solution.findMaxLength(new int[]{1, 1, 1}));
    }
}
