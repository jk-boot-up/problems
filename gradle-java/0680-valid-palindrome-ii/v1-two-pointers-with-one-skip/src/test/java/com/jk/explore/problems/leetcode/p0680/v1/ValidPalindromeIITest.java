package com.jk.explore.problems.leetcode.p0680.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ValidPalindromeIITest {

    private final ValidPalindromeII solution = new ValidPalindromeII();

    @ParameterizedTest
    @CsvSource({"aba,true", "abca,true", "abc,false", "deeee,true", "cbbcc,true"})
    void checks(String s, boolean expected) {
        assertEquals(expected, solution.validPalindrome(s));
    }
}
