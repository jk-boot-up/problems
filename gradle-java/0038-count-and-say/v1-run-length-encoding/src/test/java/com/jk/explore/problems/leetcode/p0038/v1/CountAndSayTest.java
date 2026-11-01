package com.jk.explore.problems.leetcode.p0038.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CountAndSayTest {

    private final CountAndSay solution = new CountAndSay();

    @ParameterizedTest
    @CsvSource({"1,1", "2,11", "3,21", "4,1211", "5,111221", "6,312211"})
    void terms(int n, String expected) {
        assertEquals(expected, solution.countAndSay(n));
    }
}
