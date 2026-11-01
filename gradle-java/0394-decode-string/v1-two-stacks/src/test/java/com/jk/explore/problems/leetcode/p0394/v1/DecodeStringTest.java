package com.jk.explore.problems.leetcode.p0394.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DecodeStringTest {

    private final DecodeString solution = new DecodeString();

    @ParameterizedTest
    @CsvSource({"3[a]2[bc],aaabcbc", "3[a2[c]],accaccacc", "2[abc]3[cd]ef,abcabccdcdcdef", "10[a],aaaaaaaaaa"})
    void decodes(String s, String expected) {
        assertEquals(expected, solution.decodeString(s));
    }
}
