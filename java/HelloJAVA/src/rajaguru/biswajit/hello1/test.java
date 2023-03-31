package rajaguru.biswajit.hello1;

public class test {
    public static void main(String[] args) {
        Student biswajit = new Student(
                "Biswajit Rajaguru",
                "B2-3E\nRamaniyam Rhythm Apts,\nNavalur, Chennai",
                2022);

        System.out.println(biswajit);
        biswajit.setName("Mark Twain");
        System.out.println(biswajit);

        Student anonymous = new Student();
        System.out.println(anonymous);

        Student hari = new Student("Hari");
        System.out.println(hari);

    }
}
