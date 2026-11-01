package com.jk.explore.problems.leetcode.p1249.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinRemoveToMakeValidTest {

    private final MinRemoveToMakeValid solution = new MinRemoveToMakeValid();

    @ParameterizedTest
    @CsvSource({"lee(t(c)o)de),lee(t(c)o)de", "a)b(c)d,ab(c)d", "))((,''", "(a(b(c)d),a(b(c)d)", "abc,abc", "()),()"})
    void removes(String s, String expected) {
        assertEquals(expected, solution.minRemoveToMakeValid(s));
    }
}
