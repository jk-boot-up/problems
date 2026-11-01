package com.jk.explore.problems.leetcode.p0290.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class WordPatternTest {

    private final WordPattern solution = new WordPattern();

    @ParameterizedTest
    @CsvSource({"abba,dog cat cat dog,true", "abba,dog cat cat fish,false", "aaaa,dog cat cat dog,false", "abba,dog dog dog dog,false", "ab,dog,false"})
    void checks(String pattern, String s, boolean expected) {
        assertEquals(expected, solution.wordPattern(pattern, s));
    }
}
