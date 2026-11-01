package com.jk.explore.problems.leetcode.p0299.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BullsAndCowsTest {

    private final BullsAndCows solution = new BullsAndCows();

    @ParameterizedTest
    @CsvSource({"1807,7810,1A3B", "1123,0111,1A1B", "1,0,0A0B", "1,1,1A0B", "1122,2211,0A4B", "1122,1222,3A0B"})
    void hints(String secret, String guess, String expected) {
        assertEquals(expected, solution.getHint(secret, guess));
    }
}
