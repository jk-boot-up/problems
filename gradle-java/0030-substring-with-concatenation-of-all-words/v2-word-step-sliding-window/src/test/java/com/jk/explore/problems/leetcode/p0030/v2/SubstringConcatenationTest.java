package com.jk.explore.problems.leetcode.p0030.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SubstringConcatenationTest {

    private final SubstringConcatenation solution = new SubstringConcatenation();

    @Test
    void example1() {
        assertEquals(List.of(0, 9), solution.findSubstring("barfoothefoobarman", new String[]{"foo", "bar"}));
    }

    @Test
    void duplicateWordsNoMatch() {
        assertEquals(List.of(), solution.findSubstring("wordgoodgoodgoodbestword", new String[]{"word", "good", "best", "word"}));
    }

    @Test
    void overlappingMatches() {
        assertEquals(List.of(6, 9, 12), solution.findSubstring("barfoofoobarthefoobarman", new String[]{"bar", "foo", "the"}));
    }

    @Test
    void repeatedWord() {
        assertEquals(List.of(8), solution.findSubstring("wordgoodgoodgoodbestword", new String[]{"word", "good", "best", "good"}));
    }
}
