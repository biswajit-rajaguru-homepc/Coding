package rajaguru.biswajit.hello1;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class StreamDemo {
    public static void main(String[] args) {

        ArrayList<Student> studentList = new ArrayList<>();
        studentList.add(new Student("Biswajit","Rourkela",2022));
        studentList.add(new Student("Aparna","Bangaluru",2027));
        studentList.add(new Student("Gita","Rourkela",2029));

        List<String> nameList = studentList.stream().map(x -> x.getName()).map(x->x.toUpperCase()).collect(Collectors.toList());
       // System.out.println(nameList);

        List<Student> filteredList = studentList.stream().filter(x -> Pattern.matches("Bangaluru",x.getAddress())).collect(Collectors.toList()) ;
        //System.out.println(filteredList);

        /**studentList.stream().forEach(student -> {
            System.out.println(student.getName());
            System.out.println(student.getAddress());
            System.out.println(student.getClassof());
        });*/
        //String str
        //String allPlaces = studentList.stream().reduce("",(places, student) -> String::concat(places + student.getAddress()),String::concat);
        //System.out.println(allPlaces);

    }
}
