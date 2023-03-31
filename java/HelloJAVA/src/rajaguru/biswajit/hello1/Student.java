package rajaguru.biswajit.hello1;

public class Student {

    String name, address;
    int classof;
    public Student(String name, String address, int classof){
        this.name = name;
        this.address = address;
        this.classof = classof;
    }
    public Student(String name){
        this.name = name;
        this.address = "India";
        this.classof = 2050;
    }
    public Student(){
        this.name = "John Doe";
        this.address = "Timbuctoo";
        this.classof = 2027;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setAddress(String address){
        this.address = address;
    }

    public void setClassof(int classof){
        this.classof = classof;
    }

    public String getName(){
        return this.name ;
    }

    public String getAddress(){
        return this.address ;
    }

    public int getClassof(){
        return this.classof ;
    }

    @Override
    public String toString(){
        return "Name : "+this.name+"\n"+"Address :\n"+this.address+"\nGraduating Class : "+this.classof ;
    }

    public static void main(String[] args) {
        Student biswajit = new Student(
                "Biswajit Rajaguru",
                "B2-3E\nRamaniyam Rhythm Apts,\nNavalur, Chennai",
                2022);

        System.out.println(biswajit);





    }

}
