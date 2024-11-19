
public class EstadoVerde extends Estado {
	
	public void retirar(Cuenta unaCuenta, int a) {
		unaCuenta.total -= a;
	}
	
	public boolean unaCondicion(Cuenta unaCuenta) {
		return unaCuenta.total >= 0;
	}
}
