package com.jk.explore.problems.leetcode.p0981.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TimeMapTest {

    @Test
    void example() {
        TimeMap m = new TimeMap();
        m.set("foo", "bar", 1);
        assertEquals("bar", m.get("foo", 1));
        assertEquals("bar", m.get("foo", 3));
        m.set("foo", "bar2", 4);
        assertEquals("bar2", m.get("foo", 4));
        assertEquals("bar2", m.get("foo", 5));
        assertEquals("", m.get("foo", 0));
        assertEquals("", m.get("missing", 9));
    }
}
