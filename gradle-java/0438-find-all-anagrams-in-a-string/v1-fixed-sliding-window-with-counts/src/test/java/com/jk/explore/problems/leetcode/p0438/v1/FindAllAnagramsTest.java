package com.jk.explore.problems.leetcode.p0438.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindAllAnagramsTest {

    private final FindAllAnagrams solution = new FindAllAnagrams();

    @Test
    void examples() {
        assertEquals(List.of(0, 6), solution.findAnagrams("cbaebabacd", "abc"));
        assertEquals(List.of(0, 1, 2), solution.findAnagrams("abab", "ab"));
        assertEquals(List.of(), solution.findAnagrams("a", "ab"));
    }
}
