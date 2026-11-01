package com.jk.explore.problems.leetcode.p0140.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class WordBreakIITest {

    @Test
    void examples() {
        assertEquals(Set.of("cats and dog", "cat sand dog"), new HashSet<>(new WordBreakII().wordBreak("catsanddog", List.of("cat", "cats", "and", "sand", "dog"))));
        assertEquals(Set.of("pine apple pen apple", "pineapple pen apple", "pine applepen apple"),
                new HashSet<>(new WordBreakII().wordBreak("pineapplepenapple", List.of("apple", "pen", "applepen", "pine", "pineapple"))));
        assertEquals(List.of(), new WordBreakII().wordBreak("catsandog", List.of("cats", "dog", "sand", "and", "cat")));
    }
}
