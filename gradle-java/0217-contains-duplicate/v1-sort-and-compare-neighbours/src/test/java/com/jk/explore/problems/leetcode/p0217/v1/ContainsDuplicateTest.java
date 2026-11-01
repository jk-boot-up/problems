package com.jk.explore.problems.leetcode.p0217.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ContainsDuplicateTest {

    private final ContainsDuplicate solution = new ContainsDuplicate();

    @Test
    void examples() {
        assertTrue(solution.containsDuplicate(new int[]{1, 2, 3, 1}));
        assertFalse(solution.containsDuplicate(new int[]{1, 2, 3, 4}));
        assertTrue(solution.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}));
    }

    @Test
    void single() {
        assertFalse(solution.containsDuplicate(new int[]{7}));
    }
}
