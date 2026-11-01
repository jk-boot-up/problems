package com.jk.explore.problems.leetcode.p0089.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class GrayCodeTest {

    private final GrayCode solution = new GrayCode();

    @Test
    void examples() {
        assertEquals(List.of(0, 1, 3, 2), solution.grayCode(2));
        assertEquals(List.of(0, 1), solution.grayCode(1));
    }

    @Test
    void oneBitApart() {
        List<Integer> g = solution.grayCode(10);
        assertEquals(1024, new HashSet<>(g).size());
        for (int i = 0; i < g.size(); i++) assertEquals(1, Integer.bitCount(g.get(i) ^ g.get((i + 1) % g.size())));
    }
}
