package com.jk.explore.problems.string.search;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class SmallestSubstringWIthAllCharsInAnyOrderTest {

    @Test
    public void searchPattern() {
        SmallestSubstringWIthAllCharsInAnyOrder cut = new SmallestSubstringWIthAllCharsInAnyOrder();
        String smallest = cut.shortestSubstringWindow("abcdaacxayz", "aacd");
        Assertions.assertEquals( "cdaa", smallest);

    }
}
