package com.jk.explore.problems.leetcode.p0278.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FirstBadVersionTest {

    private int calls;

    private int solve(int n, int bad) {
        calls = 0;
        return new FirstBadVersion(v -> {
            calls++;
            return v >= bad;
        }).firstBadVersion(n);
    }

    @Test
    void examples() {
        assertEquals(4, solve(5, 4));
        assertEquals(1, solve(1, 1));
        assertEquals(1, solve(10, 1));
        assertEquals(10, solve(10, 10));
    }

    @Test
    void hugeRangeUsesFewCalls() {
        assertEquals(1702766719, solve(2126753390, 1702766719));
        assertTrue(calls <= 32);
        assertEquals(Integer.MAX_VALUE, solve(Integer.MAX_VALUE, Integer.MAX_VALUE));
    }
}
