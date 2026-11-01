package com.jk.explore.problems.leetcode.p0227.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BasicCalculatorIITest {

    private final BasicCalculatorII solution = new BasicCalculatorII();

    @ParameterizedTest
    @CsvSource(delimiter = '|', value = {"3+2*2|7", " 3/2 |1", " 3+5 / 2 |5", "14-3/2|13", "1-1+1|1", "0|0", "2*3*4-10/3|21", "1-5/2|-1", "42|42"})
    void evaluates(String s, int expected) {
        assertEquals(expected, solution.calculate(s));
    }
}
