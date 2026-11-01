package com.jk.explore.problems.leetcode.p0151.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReverseWordsTest {

    private final ReverseWords solution = new ReverseWords();

    @Test
    void simple() {
        assertEquals("blue is sky the", solution.reverseWords("the sky is blue"));
    }

    @Test
    void trimsOuterSpaces() {
        assertEquals("world hello", solution.reverseWords("  hello world  "));
    }

    @Test
    void collapsesInnerSpaces() {
        assertEquals("example good a", solution.reverseWords("a good   example"));
    }
}
