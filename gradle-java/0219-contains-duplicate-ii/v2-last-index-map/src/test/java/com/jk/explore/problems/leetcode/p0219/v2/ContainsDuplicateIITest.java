package com.jk.explore.problems.leetcode.p0219.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ContainsDuplicateIITest {

    private final ContainsDuplicateII solution = new ContainsDuplicateII();

    @Test
    void farApartButWithinK() {
        assertTrue(solution.containsNearbyDuplicate(new int[]{1, 2, 3, 1}, 3));
    }

    @Test
    void adjacent() {
        assertTrue(solution.containsNearbyDuplicate(new int[]{1, 0, 1, 1}, 1));
    }

    @Test
    void tooFar() {
        assertFalse(solution.containsNearbyDuplicate(new int[]{1, 2, 3, 1, 2, 3}, 2));
    }
}
