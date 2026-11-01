package com.jk.explore.problems.leetcode.p0455.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AssignCookiesTest {

    private final AssignCookies solution = new AssignCookies();

    @Test
    void examples() {
        assertEquals(1, solution.findContentChildren(new int[]{1, 2, 3}, new int[]{1, 1}));
        assertEquals(2, solution.findContentChildren(new int[]{1, 2}, new int[]{1, 2, 3}));
        assertEquals(0, solution.findContentChildren(new int[]{1}, new int[]{}));
        assertEquals(2, solution.findContentChildren(new int[]{10, 9, 8, 7}, new int[]{5, 6, 7, 8}));
    }
}
