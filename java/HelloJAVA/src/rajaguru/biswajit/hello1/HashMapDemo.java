package rajaguru.biswajit.hello1;

import java.util.HashMap;
import java.util.Map.Entry;


public class HashMapDemo {

    public static void main(String[] args) {

        HashMap<String, Integer> hashmap = new HashMap<>();
        hashmap.put("munu", 40);
        hashmap.put("minu", 35);
        hashmap.put("nana", 74);

        System.out.println(hashmap);
        System.out.println(hashmap.size());
        if (hashmap.containsKey("munu")) System.out.println("Munu's age is : " + hashmap.get("munu"));

        for(String key : hashmap.keySet()) System.out.println("The age of "+key+" is "+hashmap.get(key));

        for(Entry<String,Integer> entry : hashmap.entrySet())
            System.out.println("Entry: Key = "+entry.getKey()+", Value = "+entry.getValue());



    }


}
