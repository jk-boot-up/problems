package com.jk.explore.problems.leetcode.p1838.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MostFrequentAfterIncrementsTest {

    private final MostFrequentAfterIncrements solution = new MostFrequentAfterIncrements();

    @Test
    void examples() {
        assertEquals(3, solution.maxFrequency(new int[]{1, 2, 4}, 5));
        assertEquals(2, solution.maxFrequency(new int[]{1, 4, 8, 13}, 5));
        assertEquals(1, solution.maxFrequency(new int[]{3, 9, 6}, 2));
        assertEquals(4, solution.maxFrequency(new int[]{7, 7, 7, 7}, 1));
    }
}
