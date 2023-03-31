package rajaguru.biswajit.hello1;

import java.util.TreeMap;
import java.util.Map.Entry ;


public class TreeMapDemo {
    public static void main(String[] args) {

        TreeMap<Integer, String > treemap = new TreeMap<>();
        treemap.put(5,"Biswajit");
        treemap.put(1,"Aparna");
        treemap.put(7,"Gorachand");
        treemap.put(2,"Gitanjali");

        System.out.println(treemap);

        for(int key : treemap.keySet())
            System.out.println("treemap("+key+") = "+treemap.get(key));

        for(Entry<Integer, String> entry : treemap.entrySet())
            System.out.println("entry ("+entry.getKey()+", "+entry.getValue()+")");




    }
}
