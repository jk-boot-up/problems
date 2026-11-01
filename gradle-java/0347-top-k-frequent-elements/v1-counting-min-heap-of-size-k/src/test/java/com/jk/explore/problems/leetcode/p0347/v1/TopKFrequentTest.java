package com.jk.explore.problems.leetcode.p0347.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TopKFrequentTest {

    private final TopKFrequent solution = new TopKFrequent();

    private static Set<Integer> set(int[] a) {
        Set<Integer> s = new HashSet<>();
        for (int x : a) s.add(x);
        return s;
    }

    @Test
    void examples() {
        assertEquals(Set.of(1, 2), set(solution.topKFrequent(new int[]{1, 1, 1, 2, 2, 3}, 2)));
        assertEquals(Set.of(1), set(solution.topKFrequent(new int[]{1}, 1)));
    }

    @Test
    void negatives() {
        assertEquals(Set.of(-1, 2), set(solution.topKFrequent(new int[]{4, -1, -1, 2, -1, 2, 3}, 2)));
    }
}
