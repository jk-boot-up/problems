package com.jk.explore.problems.leetcode.p0047.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PermutationsIITest {

    private final PermutationsII solution = new PermutationsII();

    @Test
    void duplicates() {
        assertEquals(List.of(List.of(1, 1, 2), List.of(1, 2, 1), List.of(2, 1, 1)), solution.permuteUnique(new int[]{1, 1, 2}));
    }

    @Test
    void distinct() {
        assertEquals(6, solution.permuteUnique(new int[]{1, 2, 3}).size());
    }
}
