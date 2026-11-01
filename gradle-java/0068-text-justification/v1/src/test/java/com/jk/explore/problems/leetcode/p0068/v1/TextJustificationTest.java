package com.jk.explore.problems.leetcode.p0068.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TextJustificationTest {

    private final TextJustification solution = new TextJustification();

    @Test
    void example1() {
        String[] words = {"This", "is", "an", "example", "of", "text", "justification."};
        assertEquals(List.of("This    is    an", "example  of text", "justification.  "), solution.fullJustify(words, 16));
    }

    @Test
    void lastLineLeftJustified() {
        String[] words = {"What", "must", "be", "acknowledgment", "shall", "be"};
        assertEquals(List.of("What   must   be", "acknowledgment  ", "shall be        "), solution.fullJustify(words, 16));
    }

    @Test
    void singleWord() {
        assertEquals(List.of("hi   "), solution.fullJustify(new String[]{"hi"}, 5));
    }
}
