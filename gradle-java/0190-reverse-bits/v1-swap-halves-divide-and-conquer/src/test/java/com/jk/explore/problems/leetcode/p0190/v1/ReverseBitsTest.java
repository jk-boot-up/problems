package com.jk.explore.problems.leetcode.p0190.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReverseBitsTest {

    private final ReverseBits solution = new ReverseBits();

    @Test
    void example1() {
        assertEquals(964176192, solution.reverseBits(43261596));
    }

    @Test
    void highBit() {
        assertEquals(-1073741825, solution.reverseBits(0b11111111111111111111111111111101));
    }

    @Test
    void one() {
        assertEquals(Integer.MIN_VALUE, solution.reverseBits(1));
    }
}
