package com.jk.explore.problems.leetcode.p0841.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KeysAndRoomsTest {

    private final KeysAndRooms solution = new KeysAndRooms();

    @Test
    void examples() {
        assertTrue(solution.canVisitAllRooms(List.of(List.of(1), List.of(2), List.of(3), List.of())));
        assertFalse(solution.canVisitAllRooms(List.of(List.of(1, 3), List.of(3, 0, 1), List.of(2), List.of(0))));
    }
}
