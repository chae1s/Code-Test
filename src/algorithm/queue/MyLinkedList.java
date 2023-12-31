package algorithm.queue;

public class MyLinkedList {
    private Node start;
    private static class Node {
        private int data;
        private Node link;

        public Node(int data) {
            this.data = data;
        }

        public Node(int data, Node link) {
            this.data = data;
            this.link = link;
        }
    }

    // add : 제일 뒤에 data 추가
    public void add(int data) {
        // 1. start == null (LinkedList가 비어있을 때)
        if (start == null) {
            start = new Node(data);
        }

        // 2. 아니라면, link가 null인 노드가 나올 때까지
        else {
            Node head = start;
            while (head.link != null) {
                head = head.link;
            }

            head.link = new Node(data);
        }
    }

    // remove : idx번 째 데이터를 회수 및 노드 제거
    public int remove(int idx) {
        if (idx == 0) {
            int value = start.data;
            start = start.link;
            return value;

        } else {
            int i = 0;
            Node head = start;
            Node prev = start;
            while (i < idx) {
                prev = head;
                head = head.link;
                i++;
            }

            prev.link = head.link;

            return head.data;
        }
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder("[");
        Node head = start;
        while (head != null) {
            builder.append(head.data);
            if (head.link != null) {
                builder.append(", ");
            }
            head = head.link;
        }

        builder.append("]");

        return builder.toString();

    }

    public static void main(String[] args) {
        MyLinkedList linkedList = new MyLinkedList();
        linkedList.add(1);
        linkedList.add(2);
        linkedList.add(3);

        System.out.println(linkedList);
        System.out.println(linkedList.remove(0));
        System.out.println(linkedList.remove(1));
        System.out.println(linkedList.remove(0));
    }

}
