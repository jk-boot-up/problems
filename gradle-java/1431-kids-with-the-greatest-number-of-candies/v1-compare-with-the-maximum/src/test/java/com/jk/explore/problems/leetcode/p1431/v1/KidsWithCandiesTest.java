package com.jk.explore.problems.leetcode.p1431.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KidsWithCandiesTest {

    private final KidsWithCandies solution = new KidsWithCandies();

    @Test
    void examples() {
        assertEquals(List.of(true, true, true, false, true), solution.kidsWithCandies(new int[]{2, 3, 5, 1, 3}, 3));
        assertEquals(List.of(true, false, false, false, false), solution.kidsWithCandies(new int[]{4, 2, 1, 1, 2}, 1));
    }
}
