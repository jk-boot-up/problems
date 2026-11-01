package com.jk.explore.problems.leetcode.p0678.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ValidParenthesisStringTest {

    private final ValidParenthesisString solution = new ValidParenthesisString();

    @ParameterizedTest
    @CsvSource({"'()',true", "'(*)',true", "'(*))',true", "')(',false", "'((*',false", "'*',true"})
    void checks(String s, boolean expected) {
        assertEquals(expected, solution.checkValidString(s));
    }
}
