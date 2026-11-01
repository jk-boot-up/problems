package com.jk.explore.problems.leetcode.p0046.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PermutationsTest {

    private final Permutations solution = new Permutations();

    @Test
    void three() {
        assertEquals(Set.of(List.of(1, 2, 3), List.of(1, 3, 2), List.of(2, 1, 3), List.of(2, 3, 1), List.of(3, 1, 2), List.of(3, 2, 1)),
                new HashSet<>(solution.permute(new int[]{1, 2, 3})));
    }

    @Test
    void count() {
        assertEquals(720, solution.permute(new int[]{1, 2, 3, 4, 5, 6}).size());
    }

    @Test
    void single() {
        assertEquals(List.of(List.of(1)), solution.permute(new int[]{1}));
    }
}
