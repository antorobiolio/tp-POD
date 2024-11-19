public abstract class CuentaBancaria {
	int total = 0 ;
	boolean abierta = true;
	
	public void Cerrar() {
		abierta = false;
		System.out.println("Ha cerrado la cuenta.");
	}
	
	public int getBalance() {
		return total;
	}

}




