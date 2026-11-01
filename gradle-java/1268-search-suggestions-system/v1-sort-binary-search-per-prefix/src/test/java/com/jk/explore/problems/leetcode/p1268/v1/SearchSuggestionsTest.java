package com.jk.explore.problems.leetcode.p1268.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SearchSuggestionsTest {

    private final SearchSuggestions solution = new SearchSuggestions();

    @Test
    void example() {
        List<String> top = List.of("mobile", "moneypot", "monitor"), mouse = List.of("mouse", "mousepad");
        assertEquals(List.of(top, top, mouse, mouse, mouse),
                solution.suggestedProducts(new String[]{"mobile", "mouse", "moneypot", "monitor", "mousepad"}, "mouse"));
    }

    @Test
    void noMatches() {
        assertEquals(List.of(List.of("havana"), List.of("havana"), List.of("havana"), List.of("havana"), List.of("havana"), List.of("havana")),
                solution.suggestedProducts(new String[]{"havana"}, "havana"));
        assertEquals(List.of(List.of(), List.of()), solution.suggestedProducts(new String[]{"abc"}, "xy"));
    }
}
