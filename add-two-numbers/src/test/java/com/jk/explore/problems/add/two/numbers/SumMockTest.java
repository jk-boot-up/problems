package com.jk.explore.problems.add.two.numbers;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;

import java.util.LinkedList;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.when;
import static org.mockito.MockitoAnnotations.openMocks;

public class SumMockTest {

    @Mock
    private Sum sum;

    @BeforeEach
    void setUp() {
        openMocks(this);
    }

    @Test
    void addTwoNumbers() {
        // n1 = 21
        LinkedList<Integer> n1 = new LinkedList<>();
        n1.add(1);
        n1.add(2);
        // n2 = 43
        LinkedList<Integer> n2 = new LinkedList<>();
        n2.add(3);
        n2.add(4);
        LinkedList<Integer> sum = new LinkedList<>();
        sum.add(4);
        sum.add(6);
        // sum = 12 + 34 = 46;
        when(this.sum.add(n1, n2)).thenReturn(sum);
        LinkedList<Integer> results = this.sum.add(n1, n2);
        assertEquals(results, sum);
    }


}
