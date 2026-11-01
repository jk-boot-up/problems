package com.jk.explore.problems.leetcode.p0709.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ToLowerCaseTest {

    private final ToLowerCase solution = new ToLowerCase();

    @ParameterizedTest
    @CsvSource({"Hello,hello", "here,here", "LOVELY,lovely", "A1-Z,a1-z"})
    void lowers(String s, String expected) {
        assertEquals(expected, solution.toLowerCase(s));
    }
}
