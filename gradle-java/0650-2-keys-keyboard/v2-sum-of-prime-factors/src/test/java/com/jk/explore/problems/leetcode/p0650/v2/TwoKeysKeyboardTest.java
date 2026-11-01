package com.jk.explore.problems.leetcode.p0650.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TwoKeysKeyboardTest {

    private final TwoKeysKeyboard solution = new TwoKeysKeyboard();

    @ParameterizedTest
    @CsvSource({"1,0", "2,2", "3,3", "4,4", "6,5", "9,6", "997,997", "1000,21"})
    void steps(int n, int expected) {
        assertEquals(expected, solution.minSteps(n));
    }
}
