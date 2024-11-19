import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Pedro {
	@Test
	void test_ingresar_T() {
		Cuenta Madre = new Cuenta(0);
		Madre.ingresar(10);
		System.out.println(Madre.total);
		assertEquals(10,Madre.total,0);
	}
	
	@Test
	void test_ingresar_F() {
		Cuenta cuentaIngresarBien = new Cuenta(0);
		cuentaIngresarBien.ingresar(10);
		System.out.println(cuentaIngresarBien.total);
		assertEquals(100,cuentaIngresarBien.total,0);
	}
	
	@Test
	void test_retirar_T() {
		Cuenta cuentaRetirarBien = new Cuenta(0);
		cuentaRetirarBien.ingresar(10);
		cuentaRetirarBien.retirar(5);
		System.out.println(cuentaRetirarBien.total);
		assertEquals(5,cuentaRetirarBien.total,0);
	}
	
	@Test
	void test_retirar_F() {
		Cuenta cuentaRetirarMal = new Cuenta(0);
		cuentaRetirarMal.ingresar(10);
		cuentaRetirarMal.retirar(20);
		System.out.println(cuentaRetirarMal.total);
		assertEquals(5,cuentaRetirarMal.total,0);
	}

	@Test
	void test_retirar_Rojo() {
		Cuenta cuentaRetirarRojo = new Cuenta(0);
		cuentaRetirarRojo.ingresar(10);
		cuentaRetirarRojo.retirar(20);
		System.out.println(cuentaRetirarRojo.total);
		cuentaRetirarRojo.retirar(5);
		System.out.println(cuentaRetirarRojo.total);
		assertEquals(-15,cuentaRetirarRojo.total,0);
		//No funciona el estadoRojo como debería, sigue retirando
	}
}
