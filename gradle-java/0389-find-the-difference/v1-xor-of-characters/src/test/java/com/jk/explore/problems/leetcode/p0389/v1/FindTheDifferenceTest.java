package com.jk.explore.problems.leetcode.p0389.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindTheDifferenceTest {

    private final FindTheDifference solution = new FindTheDifference();

    @Test
    void examples() {
        assertEquals('e', solution.findTheDifference("abcd", "abcde"));
        assertEquals('y', solution.findTheDifference("", "y"));
        assertEquals('a', solution.findTheDifference("a", "aa"));
    }
}
