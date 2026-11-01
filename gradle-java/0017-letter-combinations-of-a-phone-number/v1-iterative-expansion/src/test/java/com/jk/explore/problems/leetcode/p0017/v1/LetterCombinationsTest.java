package com.jk.explore.problems.leetcode.p0017.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LetterCombinationsTest {

    private final LetterCombinations solution = new LetterCombinations();

    @Test
    void twoDigits() {
        assertEquals(List.of("ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"), solution.letterCombinations("23"));
    }

    @Test
    void empty() {
        assertEquals(List.of(), solution.letterCombinations(""));
    }

    @Test
    void fourLetterKey() {
        assertEquals(List.of("p", "q", "r", "s"), solution.letterCombinations("7"));
    }
}
