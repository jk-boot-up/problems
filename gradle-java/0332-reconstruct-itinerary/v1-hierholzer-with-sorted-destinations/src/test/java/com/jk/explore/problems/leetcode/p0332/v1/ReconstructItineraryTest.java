package com.jk.explore.problems.leetcode.p0332.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReconstructItineraryTest {

    private final ReconstructItinerary solution = new ReconstructItinerary();

    @Test
    void examples() {
        assertEquals(List.of("JFK", "MUC", "LHR", "SFO", "SJC"),
                solution.findItinerary(List.of(List.of("MUC", "LHR"), List.of("JFK", "MUC"), List.of("SFO", "SJC"), List.of("LHR", "SFO"))));
        assertEquals(List.of("JFK", "ATL", "JFK", "SFO", "ATL", "SFO"),
                solution.findItinerary(List.of(List.of("JFK", "SFO"), List.of("JFK", "ATL"), List.of("SFO", "ATL"), List.of("ATL", "JFK"), List.of("ATL", "SFO"))));
    }

    @Test
    void deadEndFirst() {
        assertEquals(List.of("JFK", "NRT", "JFK", "KUL"),
                solution.findItinerary(List.of(List.of("JFK", "KUL"), List.of("JFK", "NRT"), List.of("NRT", "JFK"))));
    }
}
