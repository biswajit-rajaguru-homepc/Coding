package rajaguru.biswajit.hello1;

public class Hello1 {



    public static void main(String[] args) {

        int[][] matrix = {
                            {1, 2, 3 },
                            {4, 5, 6 },
                            {7, 8, 9 }
        };

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3 ; j++) {
                System.out.print(matrix[i][j]+"  ");
            }
            System.out.print("\n");

        }

        //System.out.println(matrix[0][1]);

        int[] ar = {9,4,6,76,567,44,45,555,4};
        for(int i : ar ) System.out.print(i + "  ");

        System.out.println();
        for (int i : ar ) {

            System.out.print(i + "  ");

        }



    }
}
