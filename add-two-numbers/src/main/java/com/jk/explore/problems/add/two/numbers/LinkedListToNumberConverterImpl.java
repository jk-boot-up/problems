package com.jk.explore.problems.add.two.numbers;

import java.util.Iterator;
import java.util.LinkedList;

public class LinkedListToNumberConverterImpl implements LinkedListToNumberConverter {
    @Override
    public int convert(LinkedList<Integer> linkedList) {
        assert linkedList != null;
        Iterator<Integer> listIterator = linkedList.iterator();
        int number = 0;
        int digitWeight = 1;
        while (listIterator.hasNext()) {
            Integer digit = listIterator.next();
            number = number + (digit * digitWeight);
            digitWeight =  digitWeight * 10;
        }
        return number;
    }
}
