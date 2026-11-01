package com.jk.explore.problems.leetcode.p1207.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class UniqueOccurrencesTest {

    private final UniqueOccurrences solution = new UniqueOccurrences();

    @Test
    void examples() {
        assertTrue(solution.uniqueOccurrences(new int[]{1, 2, 2, 1, 1, 3}));
        assertFalse(solution.uniqueOccurrences(new int[]{1, 2}));
        assertTrue(solution.uniqueOccurrences(new int[]{-3, 0, 1, -3, 1, 1, 1, -3, 10, 0}));
    }
}
