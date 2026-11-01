package com.jk.explore.problems.leetcode.p0443.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class StringCompressionTest {

    private final StringCompression solution = new StringCompression();

    private String run(String s) {
        char[] c = s.toCharArray();
        return new String(c, 0, solution.compress(c));
    }

    @Test
    void examples() {
        assertEquals("a2b2c3", run("aabbccc"));
        assertEquals("a", run("a"));
        assertEquals("ab12", run("abbbbbbbbbbbb"));
    }
}
