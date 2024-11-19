import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Cuenta {
	
	int total;
	List<Estado> estados;
	Estado estadoActual;
	
	public Cuenta(int nuevo_total) {
		this.estadoActual = new EstadoVerde();
		this.total = nuevo_total;
		this.estados = new ArrayList<>();
		
		this.estados.add(new EstadoVerde());
		this.estados.add(new EstadoRojo());
	}
	
	public void ingresar(int a) {
		this.estadoActual.ingresar(this, a);
		this.estadoActual = this.estados.stream().filter(estado->estado.unaCondicion(this)).collect(Collectors.toList()).get(0);

	}
	
	public void retirar(int a) {
		this.estadoActual.retirar(this, a);
	}
		
}