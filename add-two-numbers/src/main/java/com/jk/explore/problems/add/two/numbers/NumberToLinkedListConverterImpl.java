package com.jk.explore.problems.add.two.numbers;

import java.util.LinkedList;
import java.util.List;

public class NumberToLinkedListConverterImpl implements NumberToLinkedListConverter {
    @Override
    public LinkedList<Integer> convert(int number) {
        if(number < 0) {
            return null;
        }
        int remainder = 0;
        LinkedList<Integer> linkedList = new LinkedList<>();
        if(number == 0) {
            linkedList.add(0);
            return linkedList;
        }
        while(number > 0) {
            int digit = number % 10;
            number = number / 10;
            linkedList.add(digit);
        }
        return linkedList;
    }
}
