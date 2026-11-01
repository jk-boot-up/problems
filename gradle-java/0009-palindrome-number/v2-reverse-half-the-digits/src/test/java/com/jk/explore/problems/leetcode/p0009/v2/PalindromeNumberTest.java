package com.jk.explore.problems.leetcode.p0009.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PalindromeNumberTest {

    private final PalindromeNumber solution = new PalindromeNumber();

    @ParameterizedTest
    @CsvSource({"121,true", "-121,false", "10,false", "0,true", "1221,true", "12321,true", "2147483647,false"})
    void checks(int x, boolean expected) {
        assertEquals(expected, solution.isPalindrome(x));
    }
}
