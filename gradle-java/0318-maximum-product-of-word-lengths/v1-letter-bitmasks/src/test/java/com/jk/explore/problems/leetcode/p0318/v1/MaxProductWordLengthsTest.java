package com.jk.explore.problems.leetcode.p0318.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaxProductWordLengthsTest {

    private final MaxProductWordLengths solution = new MaxProductWordLengths();

    @Test
    void examples() {
        assertEquals(16, solution.maxProduct(new String[]{"abcw", "baz", "foo", "bar", "xtfn", "abcdef"}));
        assertEquals(4, solution.maxProduct(new String[]{"a", "ab", "abc", "d", "cd", "bcd", "abcd"}));
        assertEquals(0, solution.maxProduct(new String[]{"a", "aa", "aaa", "aaaa"}));
    }
}
