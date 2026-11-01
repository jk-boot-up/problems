package com.jk.explore.problems.leetcode.p0032.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestValidParenthesesTest {

    private final LongestValidParentheses solution = new LongestValidParentheses();

    @ParameterizedTest
    @CsvSource({"'(()',2", "')()())',4", "'',0", "'()(()',2", "'()(())',6"})
    void lengths(String s, int expected) {
        assertEquals(expected, solution.longestValidParentheses(s));
    }
}
