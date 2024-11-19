public class Main {
    public static void main(String[] args) {
        Cuenta cuentaNueva = new Cuenta(0);
        cuentaNueva.ingresar(1500);
        System.out.println(cuentaNueva.total);
        cuentaNueva.ingresar(100);
        System.out.println(cuentaNueva.total);
        System.out.println(cuentaNueva.estadoActual);
        cuentaNueva.retirar(400);
        System.out.println(cuentaNueva.total);
        cuentaNueva.retirar(4000);
        System.out.println(cuentaNueva.total);
        cuentaNueva.retirar(400);
        System.out.println(cuentaNueva.estadoActual);

    }
}
