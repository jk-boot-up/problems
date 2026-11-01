package com.jk.explore.problems.leetcode.p0767.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReorganizeStringTest {

    private final ReorganizeString solution = new ReorganizeString();

    private void assertValid(String input, String out) {
        assertEquals(input.length(), out.length());
        char[] a = input.toCharArray(), b = out.toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        assertArrayEquals(a, b);
        for (int i = 1; i < out.length(); i++) assertNotEquals(out.charAt(i - 1), out.charAt(i), out);
    }

    @Test
    void possible() {
        for (String s : new String[]{"aab", "a", "ab", "aabb", "vvvlo", "bfrbs", "aaabbbccc", "zzzzaaabc", "abbabbaaab"}) assertValid(s, solution.reorganizeString(s));
    }

    @Test
    void impossible() {
        assertEquals("", solution.reorganizeString("aaab"));
        assertEquals("", solution.reorganizeString("aa"));
    }
}
