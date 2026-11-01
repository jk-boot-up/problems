package com.jk.explore.problems.leetcode.p1405.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestHappyStringTest {

    private final LongestHappyString solution = new LongestHappyString();

    private void check(int a, int b, int c, int expectedLength) {
        String s = solution.longestDiverseString(a, b, c);
        assertEquals(expectedLength, s.length(), s);
        assertFalse(s.contains("aaa") || s.contains("bbb") || s.contains("ccc"), s);
        assertTrue(s.chars().filter(ch -> ch == 'a').count() <= a);
        assertTrue(s.chars().filter(ch -> ch == 'b').count() <= b);
        assertTrue(s.chars().filter(ch -> ch == 'c').count() <= c);
    }

    @Test
    void examples() {
        check(1, 1, 7, 8);
        check(7, 1, 0, 5);
        check(2, 2, 1, 5);
        check(0, 0, 5, 2);
        check(4, 4, 4, 12);
    }
}
