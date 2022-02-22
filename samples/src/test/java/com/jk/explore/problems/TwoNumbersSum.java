package com.jk.explore.problems;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.lang.reflect.Array;
import java.util.LinkedList;

public class TwoNumbersSum {

    @Getter
    @Setter
    @NoArgsConstructor
    static class DigitNode implements Node<Integer>{
        private Integer data;
        private Node<Integer> next;
        DigitNode(Integer data, Node<Integer> next) {
            if(data < 0 || data > 9) {
                throw new RuntimeException("data value should not be < 0 or > 9. Given digit value is: "+data);
            }
            java.util.LinkedList s = new java.util.LinkedList<>();
            this.data = data;
            this.next = next;
        }

    }

    interface Node<T> {
        T getData();
        Node<T> getNext();
        void setNext(Node<T> next);
    }

    class NodeImpl<T> implements Node<T> {
        private T data;
        private Node<T> next = null;

        public NodeImpl(T data) {
            this.data = data;
        }

        @Override
        public T getData() {
            return data;
        }

        @Override
        public Node<T> getNext() {
            return next;
        }

        @Override
        public void setNext(Node<T> next) {
            this.next = next;
        }
    }

    interface LinkedList<T> {
        public T getFirst();
        public T getLast();
        void addFirst(T t);
        void addLast(T t);
        Object[] toArray();
    }

    class LinkedListImpl<T> implements LinkedList<T> {
        private Node<T> firstNode;
        private Node<T> lastNode;
        private int size;

        public LinkedListImpl() {
        }

        @Override
        public T getFirst() {
            if(firstNode == null) {
                return null;
            }
            return firstNode.getData();
        }

        @Override
        public T getLast() {
            if(lastNode == null) {
                return null;
            }
            return lastNode.getData();
        }

        @Override
        public void addFirst(T t) {
            Node<T> newNode = new NodeImpl<>(t);
            if(firstNode == null) {
                firstNode = newNode;
                lastNode = newNode;
            } else {
                newNode.setNext(firstNode);
                firstNode = newNode;
            }
            size++;
        }

        @Override
        public void addLast(T t) {
            Node<T> newNode = new NodeImpl<>(t);
            if(lastNode == null) {
                firstNode = newNode;
                lastNode = newNode;
            } else {
                lastNode.setNext(newNode);
                lastNode = newNode;
            }
            size++;
        }

        @Override
        public Object[] toArray() {
            if(firstNode == null) {
                return null;
            }
            Object[] elements = new Object[size];
            int i=0;
            for(Node<T> currentNode = firstNode; currentNode != null; currentNode = currentNode.getNext()) {
                elements[i] = currentNode.getData();
                i++;
            }
           return elements;
        }
    }





}
