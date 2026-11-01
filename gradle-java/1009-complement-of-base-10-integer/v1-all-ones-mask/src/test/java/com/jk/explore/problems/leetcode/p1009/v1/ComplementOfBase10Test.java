package com.jk.explore.problems.leetcode.p1009.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ComplementOfBase10Test {

    private final ComplementOfBase10 solution = new ComplementOfBase10();

    @ParameterizedTest
    @CsvSource({"5,2", "7,0", "10,5", "0,1", "1,0"})
    void complements(int n, int expected) {
        assertEquals(expected, solution.bitwiseComplement(n));
    }
}
