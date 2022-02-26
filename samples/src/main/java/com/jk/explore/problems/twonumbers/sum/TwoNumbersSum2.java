package com.jk.explore.problems.twonumbers.sum;

public class TwoNumbersSum2 {

    public Node addTwoNumbers(Node firstList, Node secondList) {
        Node sumList = new Node(0, null);
        int digit1=0;
        int digit2=0;
        int sum = 0;
        int carrier = 0;
        int digit=0;
        Node currentNode = sumList;
        while(firstList != null || secondList != null) {
            digit1 =  firstList != null ? firstList.value : 0;
            digit2 = secondList != null ? secondList.value : 0;
            sum = digit1 + digit2;
            digit = (digit1 + digit2 + carrier) % 10;
            carrier = sum / 10;
            currentNode.next = new Node(digit, null);
            currentNode = currentNode.next;
            firstList = firstList.next;
            secondList = secondList.next;
        }
        if(carrier != 0) {
            currentNode.next = new Node(carrier, null);
        }

        return sumList.next;

    }

}

class Node {
    int value;
    Node next;
    Node(int value, Node next) {
        this.value = value;
        this.next = next;
    }

}
