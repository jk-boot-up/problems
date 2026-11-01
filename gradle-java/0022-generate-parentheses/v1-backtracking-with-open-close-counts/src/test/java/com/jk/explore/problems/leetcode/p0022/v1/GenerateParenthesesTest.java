package com.jk.explore.problems.leetcode.p0022.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class GenerateParenthesesTest {

    private final GenerateParentheses solution = new GenerateParentheses();

    @Test
    void three() {
        assertEquals(List.of("((()))", "(()())", "(())()", "()(())", "()()()"), solution.generateParenthesis(3));
    }

    @Test
    void one() {
        assertEquals(List.of("()"), solution.generateParenthesis(1));
    }

    @Test
    void catalanCount() {
        assertEquals(1430, solution.generateParenthesis(8).size());
    }
}
