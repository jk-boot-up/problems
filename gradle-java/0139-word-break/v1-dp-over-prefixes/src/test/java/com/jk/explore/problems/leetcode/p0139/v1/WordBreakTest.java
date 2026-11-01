package com.jk.explore.problems.leetcode.p0139.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class WordBreakTest {

    private final WordBreak solution = new WordBreak();

    @Test
    void examples() {
        assertTrue(solution.wordBreak("leetcode", List.of("leet", "code")));
        assertTrue(solution.wordBreak("applepenapple", List.of("apple", "pen")));
        assertFalse(solution.wordBreak("catsandog", List.of("cats", "dog", "sand", "and", "cat")));
    }

    @Test
    void longRepeated() {
        assertFalse(solution.wordBreak("a".repeat(150) + "b", List.of("a", "aa", "aaa", "aaaa")));
    }
}
