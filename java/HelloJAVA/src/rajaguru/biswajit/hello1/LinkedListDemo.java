package rajaguru.biswajit.hello1;
import java.util.LinkedList ;

public class LinkedListDemo {
    public static void main(String[] args) {

        LinkedList<String> strlist = new LinkedList<>();
        String[] name = {"B","I","S","W","A","J","I","T"};
        for(String letter : name) strlist.add(letter);
        System.out.println(strlist);


    }
}
