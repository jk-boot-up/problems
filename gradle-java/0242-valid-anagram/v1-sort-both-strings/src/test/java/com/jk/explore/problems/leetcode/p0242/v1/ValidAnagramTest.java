package com.jk.explore.problems.leetcode.p0242.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ValidAnagramTest {

    private final ValidAnagram solution = new ValidAnagram();

    @ParameterizedTest
    @CsvSource({"anagram,nagaram,true", "rat,car,false", "a,ab,false", "listen,silent,true"})
    void checks(String s, String t, boolean expected) {
        assertEquals(expected, solution.isAnagram(s, t));
    }
}
