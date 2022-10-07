package com.jk.explore.problems;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class LongestSubStringWithoutRepeatingCharsTest {

    @Test
    public void sample1() {
        LongestSubStringWithoutRepeatingChars resolver = new LongestSubStringWithoutRepeatingChars();
        assertEquals(resolver.longestSubStringLength("abcdabbcdeabc"), 5);
        assertEquals(resolver.longestSubStringLength("abcabcbb"), 3);
        assertEquals(resolver.getLongestSubstring("abcdabbcdeabc"), "bcdea");
        assertEquals(resolver.getLongestSubstring("abcabcbb"), "abc");
    }

}
