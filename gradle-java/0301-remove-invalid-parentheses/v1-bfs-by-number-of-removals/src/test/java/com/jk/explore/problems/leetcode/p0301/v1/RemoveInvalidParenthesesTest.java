package com.jk.explore.problems.leetcode.p0301.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RemoveInvalidParenthesesTest {

    private final RemoveInvalidParentheses solution = new RemoveInvalidParentheses();

    private List<String> sorted(List<String> l) {
        List<String> c = new ArrayList<>(l);
        Collections.sort(c);
        return c;
    }

    @Test
    void examples() {
        assertEquals(List.of("(())()", "()()()"), sorted(solution.removeInvalidParentheses("()())()")));
        assertEquals(List.of("(a())()", "(a)()()"), sorted(solution.removeInvalidParentheses("(a)())()")));
        assertEquals(List.of(""), solution.removeInvalidParentheses(")("));
        assertEquals(List.of("x"), solution.removeInvalidParentheses("x("));
        assertEquals(List.of("()"), solution.removeInvalidParentheses("()"));
        assertEquals(List.of("(())"), sorted(solution.removeInvalidParentheses("((())")));
    }
}
