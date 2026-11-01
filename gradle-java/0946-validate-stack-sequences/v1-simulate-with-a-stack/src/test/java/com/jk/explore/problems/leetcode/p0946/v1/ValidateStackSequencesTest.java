package com.jk.explore.problems.leetcode.p0946.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ValidateStackSequencesTest {

    private final ValidateStackSequences solution = new ValidateStackSequences();

    @Test
    void examples() {
        assertTrue(solution.validateStackSequences(new int[]{1, 2, 3, 4, 5}, new int[]{4, 5, 3, 2, 1}));
        assertFalse(solution.validateStackSequences(new int[]{1, 2, 3, 4, 5}, new int[]{4, 3, 5, 1, 2}));
        assertTrue(solution.validateStackSequences(new int[]{1}, new int[]{1}));
        assertTrue(solution.validateStackSequences(new int[]{2, 1, 0}, new int[]{1, 2, 0}));
    }
}
