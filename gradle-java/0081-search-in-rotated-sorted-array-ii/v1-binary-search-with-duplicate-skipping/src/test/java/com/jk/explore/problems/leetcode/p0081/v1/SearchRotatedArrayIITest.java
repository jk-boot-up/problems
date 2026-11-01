package com.jk.explore.problems.leetcode.p0081.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SearchRotatedArrayIITest {

    private final SearchRotatedArrayII solution = new SearchRotatedArrayII();

    @Test
    void examples() {
        assertTrue(solution.search(new int[]{2, 5, 6, 0, 0, 1, 2}, 0));
        assertFalse(solution.search(new int[]{2, 5, 6, 0, 0, 1, 2}, 3));
        assertTrue(solution.search(new int[]{1, 0, 1, 1, 1}, 0));
    }
}
