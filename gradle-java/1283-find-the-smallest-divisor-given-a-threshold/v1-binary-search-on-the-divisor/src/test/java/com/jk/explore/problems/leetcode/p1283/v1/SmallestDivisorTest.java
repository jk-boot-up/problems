package com.jk.explore.problems.leetcode.p1283.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SmallestDivisorTest {

    private final SmallestDivisor solution = new SmallestDivisor();

    @Test
    void examples() {
        assertEquals(5, solution.smallestDivisor(new int[]{1, 2, 5, 9}, 6));
        assertEquals(44, solution.smallestDivisor(new int[]{44, 22, 33, 11, 1}, 5));
        assertEquals(1, solution.smallestDivisor(new int[]{21212, 10101, 12121}, 1_000_000));
        assertEquals(3, solution.smallestDivisor(new int[]{2, 3, 5, 7, 11}, 11));
        assertEquals(1_000_000, solution.smallestDivisor(new int[]{1_000_000}, 1));
    }
}
