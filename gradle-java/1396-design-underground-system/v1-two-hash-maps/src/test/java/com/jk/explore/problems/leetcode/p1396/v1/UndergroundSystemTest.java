package com.jk.explore.problems.leetcode.p1396.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class UndergroundSystemTest {

    @Test
    void example() {
        UndergroundSystem u = new UndergroundSystem();
        u.checkIn(45, "Leyton", 3);
        u.checkIn(32, "Paradise", 8);
        u.checkIn(27, "Leyton", 10);
        u.checkOut(45, "Waterloo", 15);
        u.checkOut(27, "Waterloo", 20);
        u.checkOut(32, "Cambridge", 22);
        assertEquals(14.0, u.getAverageTime("Paradise", "Cambridge"), 1e-9);
        assertEquals(11.0, u.getAverageTime("Leyton", "Waterloo"), 1e-9);
        u.checkIn(10, "Leyton", 24);
        assertEquals(11.0, u.getAverageTime("Leyton", "Waterloo"), 1e-9);
        u.checkOut(10, "Waterloo", 38);
        assertEquals(12.0, u.getAverageTime("Leyton", "Waterloo"), 1e-9);
    }

    @Test
    void directionMatters() {
        UndergroundSystem u = new UndergroundSystem();
        u.checkIn(1, "A", 0);
        u.checkOut(1, "B", 5);
        u.checkIn(1, "B", 10);
        u.checkOut(1, "A", 30);
        assertEquals(5.0, u.getAverageTime("A", "B"), 1e-9);
        assertEquals(20.0, u.getAverageTime("B", "A"), 1e-9);
    }
}
