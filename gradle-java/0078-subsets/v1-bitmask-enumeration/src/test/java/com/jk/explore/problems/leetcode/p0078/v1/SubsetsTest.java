package com.jk.explore.problems.leetcode.p0078.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SubsetsTest {

    private final Subsets solution = new Subsets();

    @Test
    void three() {
        Set<List<Integer>> got = new HashSet<>(solution.subsets(new int[]{1, 2, 3}));
        assertEquals(8, got.size());
        assertTrue(got.containsAll(List.of(List.of(), List.of(1, 2, 3), List.of(2), List.of(1, 3))));
    }

    @Test
    void single() {
        assertEquals(List.of(List.of(), List.of(0)), solution.subsets(new int[]{0}));
    }
}
