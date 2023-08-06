package com.jk.explore.problems.add.two.numbers;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.LinkedList;

import static java.util.List.of;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class LinkedListToNumberConverterImplTest {

    private LinkedListToNumberConverter converter;

    @BeforeEach
    void setUp() {
        converter = new LinkedListToNumberConverterImpl();
    }

    @Test
    void convertFor3DigitNumber() {
        LinkedList<Integer> numberList = new LinkedList<>(of(3, 2, 1));
        int actual = converter.convert(numberList);
        assertEquals(123, actual);
    }

    @Test
    void convertFor1DigitNumber() {
        LinkedList<Integer> numberList = new LinkedList<>(of(4));
        assertEquals(4, converter.convert(numberList));
    }

    @Test
    void convertFor2DigitNumber() {
        LinkedList<Integer> numberList = new LinkedList<>(of(0, 1));
        assertEquals(10, converter.convert(numberList));
    }

    @Test
    void convertFor3DigitNumberAndTrailingZeroes() {
        LinkedList<Integer> numberList = new LinkedList<>(of(0, 0, 1));
        assertEquals(100, converter.convert(numberList));
    }

    @Test
    void convertFor10DigitNumber() {
        LinkedList<Integer> numberList = new LinkedList<>(of(0, 9, 8, 7, 6, 5, 4, 3, 2, 1));
        assertEquals(1234567890, converter.convert(numberList));
    }
}
