
public class EstadoRojo extends Estado {
	
	public void retirar(Cuenta unaCuenta, int a) {
		System.out.println("Pobre.");
	}
	
	public boolean unaCondicion(Cuenta unaCuenta) {
		return unaCuenta.total < 0;
	}
	
}
