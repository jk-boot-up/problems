package com.jk.explore.problems.add.two.numbers;


import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.LinkedList;

import static java.util.List.of;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class SumImplTest {

    private Sum sum;

    @BeforeEach
    void setUp() {
        sum = new SumImpl();
    }

    @Test
    void addForEqualLengthNumbers()  {
        // n1 = 456
        LinkedList<Integer> n1 = new LinkedList<>(of(6, 5, 4));
        //n2 = 897
        LinkedList<Integer> n2 = new LinkedList<>(of(7, 9, 8));
        LinkedList<Integer> sum = this.sum.add(n1, n2);
        LinkedList<Integer> expected = new LinkedList<>(of(3, 5, 3, 1));
        assertEquals(expected, sum);
    }

    @Test
    void addForUnequalLengthNumbers() {
        // n1 = 345;
        LinkedList<Integer> n1 = new LinkedList<>(of(5, 4, 3));
        // n2 = 1;
        LinkedList<Integer> n2 = new LinkedList<>(of(1));
        LinkedList<Integer> expected = new LinkedList<>(of(6, 4, 3));
        LinkedList<Integer> actual = sum.add(n1, n2);
        Assertions.assertEquals(expected, actual);
        actual = sum.add(n2, n1);
        assertEquals(expected, actual);
    }

    @Test
    void addNumbersForZero() {
        LinkedList<Integer> n1 = new LinkedList<>(of(0));
        LinkedList<Integer> expected = new LinkedList<>(of(0));
        LinkedList<Integer> actual = sum.add(n1, n1);
        assertEquals(expected, actual);
    }

    @Test
    void addNumbersForNonZero() {
        LinkedList<Integer> n1 = new LinkedList<>(of(0, 1));
        LinkedList<Integer> expected = new LinkedList<>(of(0, 2));
        LinkedList<Integer> actual = sum.add(n1, n1);
        assertEquals(expected, actual);
    }

    @Test
    void addNumbersForSingleDigitNonZero() {
        LinkedList<Integer> n1 = new LinkedList<>(of(9));
        LinkedList<Integer> expected = new LinkedList<>(of(8, 1));
        LinkedList<Integer> actual = sum.add(n1, n1);
        assertEquals(expected, actual);
    }

    @Test
    void addNumbersForCarry() {
        LinkedList<Integer> n1 = new LinkedList<>(of(9, 9));
        LinkedList<Integer> expected = new LinkedList<>(of(8, 9, 1));
        LinkedList<Integer> actual = sum.add(n1, n1);
        assertEquals(expected, actual);
    }

    @Test
    void addNumbersForNoCarry() {
        LinkedList<Integer> n1 = new LinkedList<>(of(5, 6, 7));
        LinkedList<Integer> n2 = new LinkedList<>(of(0));
        LinkedList<Integer> expected = new LinkedList<>(of(5, 6, 7));
        LinkedList<Integer> actual = sum.add(n1, n2);
        assertEquals(expected, actual);
    }

}
