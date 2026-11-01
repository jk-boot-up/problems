package com.jk.explore.problems.leetcode.p0067.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AddBinaryTest {

    private final AddBinary solution = new AddBinary();

    @ParameterizedTest
    @CsvSource({"11,1,100", "1010,1011,10101", "0,0,0", "1111,1111,11110"})
    void adds(String a, String b, String expected) {
        assertEquals(expected, solution.addBinary(a, b));
    }
}
