package com.jk.explore.problems.leetcode.p0058.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LengthOfLastWordTest {

    private final LengthOfLastWord solution = new LengthOfLastWord();

    @Test
    void simple() {
        assertEquals(5, solution.lengthOfLastWord("Hello World"));
    }

    @Test
    void trailingSpaces() {
        assertEquals(4, solution.lengthOfLastWord("   fly me   to   the moon  "));
    }

    @Test
    void singleWord() {
        assertEquals(5, solution.lengthOfLastWord("luffy"));
    }
}
