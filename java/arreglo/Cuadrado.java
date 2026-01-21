public class Cuadrado{

    public int[] calcularCuadrado(int[] arreglo){
        int[] cuadrados = new int[arreglo.length];
        for(int i=0; i<arreglo.length; i++){
            cuadrados[i] = arreglo[i]*arreglo[i];
        }
        return cuadrados;
    }
    public static void main(String[] args){

        int[] numeros = {1,2,3,4,5};
        int[] cuadradosNumeros = new Cuadrado().calcularCuadrado(numeros);
        for(int i=0; i < cuadradosNumeros.length; i++){
            System.out.println(cuadradosNumeros[i]);
        }
        
    }
}