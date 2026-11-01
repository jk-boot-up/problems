package com.jk.explore.problems.leetcode.p2390.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RemovingStarsTest {

    private final RemovingStars solution = new RemovingStars();

    @ParameterizedTest
    @CsvSource({"leet**cod*e,lecoe", "erase*****,''", "abc,abc"})
    void removes(String s, String expected) {
        assertEquals(expected, solution.removeStars(s));
    }
}
