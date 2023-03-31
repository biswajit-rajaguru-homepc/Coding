package rajaguru.biswajit.hello1;

//import rajaguru.biswajit.hello1.Utils ;


public class ClassDemo {
    public static void main(String[] args) {

    Utils.greeting();
    TestClass.method2();
    TestClass testclass = new TestClass();
    int[] array = {1,2,3,4};
    for(int i : array) {
        testclass.method1();
        TestClass.method2();
    }

        /*AbstractDemoChild dd = new AbstractDemoChild();
        dd.whoAmI();*/

    }
}
