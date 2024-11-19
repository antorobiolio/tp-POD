
public abstract class Estado {
	
	public void ingresar(Cuenta unaCuenta, int a) {
		unaCuenta.total += a;
	}
	
	abstract void retirar(Cuenta unaCuenta, int a);
	
	abstract boolean unaCondicion (Cuenta unaCuenta);

}
