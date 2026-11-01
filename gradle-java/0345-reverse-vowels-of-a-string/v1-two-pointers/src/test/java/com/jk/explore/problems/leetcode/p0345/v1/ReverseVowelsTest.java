package com.jk.explore.problems.leetcode.p0345.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReverseVowelsTest {

    private final ReverseVowels solution = new ReverseVowels();

    @ParameterizedTest
    @CsvSource({"IceCreAm,AceCreIm", "leetcode,leotcede", "xyz,xyz"})
    void reverses(String s, String expected) {
        assertEquals(expected, solution.reverseVowels(s));
    }
}
