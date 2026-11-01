package com.jk.explore.problems.leetcode.p0020.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ValidParenthesesTest {

    private final ValidParentheses solution = new ValidParentheses();

    @ParameterizedTest
    @CsvSource({"'()[]{}',true", "'(]',false", "'([])',true", "'([)]',false", "'(((',false", "')',false", "'{[]}',true"})
    void checks(String s, boolean expected) {
        assertEquals(expected, solution.isValid(s));
    }
}
