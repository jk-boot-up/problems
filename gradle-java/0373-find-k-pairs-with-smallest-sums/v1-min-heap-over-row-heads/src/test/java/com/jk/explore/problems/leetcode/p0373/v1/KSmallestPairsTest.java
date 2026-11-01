package com.jk.explore.problems.leetcode.p0373.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KSmallestPairsTest {

    private final KSmallestPairs solution = new KSmallestPairs();

    @Test
    void example1() {
        assertEquals(List.of(List.of(1, 2), List.of(1, 4), List.of(1, 6)), solution.kSmallestPairs(new int[]{1, 7, 11}, new int[]{2, 4, 6}, 3));
    }

    @Test
    void sumsOnly() {
        List<List<Integer>> out = solution.kSmallestPairs(new int[]{1, 1, 2}, new int[]{1, 2, 3}, 2);
        assertEquals(List.of(2, 2), out.stream().map(p -> p.get(0) + p.get(1)).toList());
    }

    @Test
    void allPairs() {
        assertEquals(4, solution.kSmallestPairs(new int[]{1, 2}, new int[]{3, 4}, 4).size());
    }
}
