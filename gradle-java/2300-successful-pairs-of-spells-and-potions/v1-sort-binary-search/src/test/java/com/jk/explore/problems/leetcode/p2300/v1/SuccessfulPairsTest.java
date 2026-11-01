package com.jk.explore.problems.leetcode.p2300.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SuccessfulPairsTest {

    private final SuccessfulPairs solution = new SuccessfulPairs();

    @Test
    void examples() {
        assertArrayEquals(new int[]{4, 0, 3}, solution.successfulPairs(new int[]{5, 1, 3}, new int[]{1, 2, 3, 4, 5}, 7));
        assertArrayEquals(new int[]{2, 0, 2}, solution.successfulPairs(new int[]{3, 1, 2}, new int[]{8, 5, 8}, 16));
    }
}
