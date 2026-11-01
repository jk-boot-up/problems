package com.jk.explore.problems.leetcode.p0258.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AddDigitsTest {

    private final AddDigits solution = new AddDigits();

    @ParameterizedTest
    @CsvSource({"38,2", "0,0", "9,9", "10,1", "18,9", "19,1", "2147483647,1"})
    void roots(int num, int expected) {
        assertEquals(expected, solution.addDigits(num));
    }
}
