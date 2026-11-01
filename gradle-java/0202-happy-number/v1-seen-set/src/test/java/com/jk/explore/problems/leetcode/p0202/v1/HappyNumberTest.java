package com.jk.explore.problems.leetcode.p0202.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class HappyNumberTest {

    private final HappyNumber solution = new HappyNumber();

    @ParameterizedTest
    @CsvSource({"19,true", "2,false", "1,true", "7,true", "4,false"})
    void checks(int n, boolean expected) {
        assertEquals(expected, solution.isHappy(n));
    }
}
