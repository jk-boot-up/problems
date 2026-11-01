package com.jk.explore.problems.leetcode.p0973.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KClosestPointsTest {

    private final KClosestPoints solution = new KClosestPoints();

    private static Set<List<Integer>> set(int[][] pts) {
        Set<List<Integer>> s = new HashSet<>();
        for (int[] p : pts) s.add(List.of(p[0], p[1]));
        return s;
    }

    @Test
    void examples() {
        assertEquals(Set.of(List.of(-2, 2)), set(solution.kClosest(new int[][]{{1, 3}, {-2, 2}}, 1)));
        assertEquals(Set.of(List.of(3, 3), List.of(-2, 4)), set(solution.kClosest(new int[][]{{3, 3}, {5, -1}, {-2, 4}}, 2)));
    }
}
