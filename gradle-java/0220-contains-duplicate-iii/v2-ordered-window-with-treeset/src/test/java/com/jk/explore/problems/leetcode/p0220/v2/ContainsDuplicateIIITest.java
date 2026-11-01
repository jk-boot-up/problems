package com.jk.explore.problems.leetcode.p0220.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ContainsDuplicateIIITest {

    private final ContainsDuplicateIII solution = new ContainsDuplicateIII();

    @Test
    void examples() {
        assertTrue(solution.containsNearbyAlmostDuplicate(new int[]{1, 2, 3, 1}, 3, 0));
        assertFalse(solution.containsNearbyAlmostDuplicate(new int[]{1, 5, 9, 1, 5, 9}, 2, 3));
        assertTrue(solution.containsNearbyAlmostDuplicate(new int[]{1, 0, 1, 1}, 1, 2));
    }

    @Test
    void negativesAndExtremes() {
        assertFalse(solution.containsNearbyAlmostDuplicate(new int[]{-3, 3}, 2, 4));
        assertTrue(solution.containsNearbyAlmostDuplicate(new int[]{-3, 3}, 2, 6));
        assertFalse(solution.containsNearbyAlmostDuplicate(new int[]{Integer.MIN_VALUE, Integer.MAX_VALUE}, 1, Integer.MAX_VALUE));
        assertTrue(solution.containsNearbyAlmostDuplicate(new int[]{-1, -1}, 1, 0));
    }

    @Test
    void windowLimit() {
        assertFalse(solution.containsNearbyAlmostDuplicate(new int[]{1, 2, 3, 1}, 2, 0));
        assertTrue(solution.containsNearbyAlmostDuplicate(new int[]{8, 7, 15, 1, 6, 1, 9, 15}, 1, 3));
    }
}
