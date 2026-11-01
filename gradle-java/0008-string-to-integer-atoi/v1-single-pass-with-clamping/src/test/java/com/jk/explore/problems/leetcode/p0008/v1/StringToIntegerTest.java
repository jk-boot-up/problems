package com.jk.explore.problems.leetcode.p0008.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class StringToIntegerTest {

    private final StringToInteger solution = new StringToInteger();

    @ParameterizedTest
    @CsvSource({"42,42", "'   -042',-42", "1337c0d3,1337", "0-1,0", "words and 987,0", "-91283472332,-2147483648", "2147483648,2147483647", "'',0"})
    void converts(String s, int expected) {
        assertEquals(expected, solution.myAtoi(s));
    }
}
