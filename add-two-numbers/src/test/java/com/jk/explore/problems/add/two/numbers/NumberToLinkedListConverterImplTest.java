package com.jk.explore.problems.add.two.numbers;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.LinkedList;

import static java.util.List.of;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

public class NumberToLinkedListConverterImplTest {

    private NumberToLinkedListConverter numberToLinkedListConverter;

    @BeforeEach
    void setUp() {
        numberToLinkedListConverter = new NumberToLinkedListConverterImpl();
    }

    @Test
    void testForSingleDigit() {
        LinkedList<Integer> actual = numberToLinkedListConverter.convert(0);
        LinkedList<Integer> expected = new LinkedList<>(of(0));
        assertEquals(expected, actual);
        actual = numberToLinkedListConverter.convert(6);
        expected = new LinkedList<>(of(6));
        assertEquals(expected, actual);
    }

    @Test
    void testFor2digitNumber() {
        LinkedList<Integer> actual = numberToLinkedListConverter.convert(10);
        LinkedList<Integer> expected = new LinkedList<>(of(0, 1));
        assertEquals(expected, actual);
        actual = numberToLinkedListConverter.convert(22);
        expected = new LinkedList<Integer>(of(2, 2));
        assertEquals(expected, actual);
        actual = numberToLinkedListConverter.convert(45);
        expected = new LinkedList<Integer>(of(5, 4));
        assertEquals(expected, actual);
    }

    @Test
    void testForNegativeNumber() {
        LinkedList<Integer> actual = numberToLinkedListConverter.convert(-345);
        assertNull(actual);
    }

}
