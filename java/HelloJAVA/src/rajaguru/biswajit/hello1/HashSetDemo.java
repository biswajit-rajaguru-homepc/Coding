package rajaguru.biswajit.hello1;
import java.util.HashSet;
public class HashSetDemo {

    public static void main(String[] args) {
        HashSet<String> strhash = new HashSet<>(1);
        String[] name = {"B","I","S","W","A","J","I","T"};
        for (String letter : name) strhash.add(letter);
        System.out.println(strhash);
        System.out.println("Does strhash contain Z ? " + strhash.contains("Z"));
        System.out.println("Does strhash contain B ? " + strhash.contains("B"));
        strhash.remove("B");
        System.out.println("Does strhash contain B ? " + strhash.contains("B"));
        System.out.println(strhash);
       System.out.println("Biswajit");



        
    }


}
