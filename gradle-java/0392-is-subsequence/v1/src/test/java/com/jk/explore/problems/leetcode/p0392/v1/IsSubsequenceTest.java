package com.jk.explore.problems.leetcode.p0392.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IsSubsequenceTest {

    private final IsSubsequence solution = new IsSubsequence();

    @Test
    void found() {
        assertTrue(solution.isSubsequence("abc", "ahbgdc"));
    }

    @Test
    void notFound() {
        assertFalse(solution.isSubsequence("axc", "ahbgdc"));
    }

    @Test
    void emptyIsAlwaysSubsequence() {
        assertTrue(solution.isSubsequence("", "abc"));
    }
}
