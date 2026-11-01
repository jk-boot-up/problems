package com.jk.explore.problems.leetcode.p0224.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BasicCalculatorTest {

    private final BasicCalculator solution = new BasicCalculator();

    @ParameterizedTest
    @CsvSource({"'1 + 1',2", "' 2-1 + 2 ',3", "'(1+(4+5+2)-3)+(6+8)',23", "'-(2 + 3)',-5", "'1-(     -2)',3", "'2147483647',2147483647"})
    void evaluates(String s, int expected) {
        assertEquals(expected, solution.calculate(s));
    }
}
