package rajaguru.biswajit.hello1;

import java.util.ArrayList ;

public class ArrayListDemo {

    public static void main(String[] args) {


        ArrayList<Integer> arrList = new ArrayList<>(1);
        for (int i = 0; i < 10; i++) {
            arrList.add(i);
        }
        //System.out.println(arrList + " , 5th element: " + arrList.get(4) + " , Size: " + arrList.size());

        arrList.remove(4);

        //System.out.println(arrList + " , 5th element: " + arrList.get(4) + " , Size: " + arrList.size());

        int j = 5, i=0;

        for ( ; i < j; i++) {
            System.out.println(j-- + " * " + i);
        }


    }

}
