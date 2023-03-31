package rajaguru.biswajit.hello1;
//import rajaguru.biswajit.hello1.AbstractDemoChild;

class TestClass {

    TestClass(){
        System.out.println("TestClass constructor called");
        cnt = 0;
        demo1 = new AbstractDemoChild();
        System.out.println(demo1.message);
    }

    private static int cnt;
    AbstractDemoChild demo1;

    protected void method1(){
        System.out.println("Method1 in TestClass");
        cnt++;
    }


    protected static void method2(){
        System.out.println("cnt : " + cnt);
        cnt++;

    }





}
