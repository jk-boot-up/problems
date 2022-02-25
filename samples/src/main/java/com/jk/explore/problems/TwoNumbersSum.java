package com.jk.explore.problems;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.ArrayList;
import java.util.List;


public class TwoNumbersSum {


    @Getter
    @Setter
    @NoArgsConstructor
    static class DigitNode {
        int digit;
        DigitNode next;
        public DigitNode(int digit) {
            this.digit = digit;
        }
    }

    @Getter
    @Setter
    static class DigitLinkedList {
        private DigitNode first;
        private DigitNode last;
        int size;

        public void addLast(Integer digit) {
            if(digit == null) {
                return;
            }
            if(first == null) {
                first = new DigitNode(digit);
                last = first;
                size++;
            } else {
                last.next = new DigitNode(digit);
                last = last.next;
                size++;
            }
        }

        public List<Integer> traversedList() {
            if(first == null) {
                return null;
            }
            DigitNode current = first;
            List<Integer> list = new ArrayList<>();
            while (current != null) {
                list.add(current.getDigit());
                current = current.getNext();
            }
            return list;
        }

    }

    static class Util {

        public Util() {

        }

        public DigitLinkedList getLinkedList(Integer number) {
            DigitLinkedList linkedList = new DigitLinkedList();
            Integer temp = number;
            while(temp > 0) {
                int digit = temp % 10;
                temp = temp / 10;
                linkedList.addLast(digit);
            }
            return linkedList;
        }

        public DigitLinkedList add(DigitLinkedList first, DigitLinkedList second) {
            DigitNode node1 = first.getFirst();
            DigitNode node2 = second.getFirst();
            DigitLinkedList sumDigitsList = new DigitLinkedList();
            int carryDigit = 0;
            int digitsSum = 0;
            boolean done = false;
            while(! done) {
                if(node1 != null && node2 != null) {
                    digitsSum = node1.getDigit() + node2.getDigit() + carryDigit;
                    int digitNodeValue = digitsSum % 10;
                    carryDigit = digitsSum / 10;
                    sumDigitsList.addLast(digitNodeValue);
                    node1 = node1.getNext();
                    node2 = node2.getNext();
                } else if(node1 == null & node2 != null) {
                    digitsSum = node2.getDigit() + carryDigit;
                    node2 = node2.getNext();
                    int digitNodeValue = digitsSum % 10;
                    carryDigit = digitsSum / 10;
                    sumDigitsList.addLast(digitNodeValue);
                } else if(node1 != null && node2 == null) {
                    digitsSum = node1.getDigit() + carryDigit;
                    node1 = node1.getNext();
                    int digitNodeValue = digitsSum % 10;
                    carryDigit = digitsSum / 10;
                    sumDigitsList.addLast(digitNodeValue);
                } else {
                    done = true;
                }
            };
            if(carryDigit > 0) {
                sumDigitsList.addLast(carryDigit);
            }

            return sumDigitsList;
        }

        public Integer getNumber(DigitLinkedList linkedList) {
            List<Integer> digitList = linkedList.traversedList();
            StringBuffer sb = new StringBuffer();
            for(int index=digitList.size()-1; index >-1; index--) {
                int digit = (Integer) digitList.get(index);
                sb.append(String.valueOf(digit));
            }
            return Integer.valueOf(sb.toString());
        }
    }



}
