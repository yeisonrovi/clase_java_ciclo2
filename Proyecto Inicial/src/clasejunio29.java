import java.util.Scanner;

public class clasejunio29 {
    public static void main (String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingresa un mensaje");
        String entrada = scanner.nextLine();
        System.out.println("EL mensaje que ingresaste es " + "'" + entrada + "'" );
        System.out.println("Ingresa un número");
        int numero = scanner.nextInt();
        System.out.println("EL mensaje que ingresaste es " + numero );

        if (numero%2 == 0) {

            System.out.println("El número es par");

        }else{
            System.out.println("El número es impar");
        }

        System.out.println("Ingresa un elemento");
        String elemento = scanner.nextLine();

        switch(elemento){
            case "Agua":
                System.out.println("Maestro Agua");
                break;
            case "Fuego":
                System.out.println("Maestro Fuego");
                break;
            case "Tierra":
                System.out.println("Maestro Tierra");
                break;
            case "Aire":
                System.out.println("Maestro Aire");
                break;
        }

        int contador = 1;

        while(true){
            System.out.println(":3");
            contador = contador + 1;
            if (contador == 5){
                break;
            }
        }

        int numero1 = 9;
        do{
            System.out.println(":3");
        }while(numero1>10);
        
        for(int i=7; i>0; i = i-1){
            System.out.println(i);
        }
        for(int i=0; i<=20; i = i+2){
            System.out.println(i);
        }
        for(int i=0; i<=20; i = i+2){
            if (i==8){
                break;
            }
            System.out.println(i);
        }

        // Operadores

        int var1 = 10;
        System.out.println(var1*3);
        System.out.println(Math.cbrt(var1));

        int contador1 = 0;
        contador1 = contador + 1;
        contador1 += 1;
        contador1 ++; 
        System.out.println(contador1);
        System.out.println(contador1++);  // Primero imprime y luego Suma
        System.out.println(--contador1);   // Primero resta y luego imprime 
        char caracter = 'z'; 
        System.out.println(++caracter);


        String variable3 = 5>2 ? ":)" : ":(";
        System.out.println(variable3);

        if (5>3 | 1>2){   // Equivalente al or en Python es |   // Equivalente al and en Python & // Equivalente a la negación es  (!(condicion))
            System.out.println("Lord of the ring");
        
        }

        if (5>1|3>1) {

            System.out.println("El número es par");

        }

    }
}
