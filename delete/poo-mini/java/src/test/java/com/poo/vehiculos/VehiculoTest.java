package com.poo.vehiculos;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class VehiculoTest {
    @Test
    void testEncapsulamientoYMovimiento() {
        Auto a = new Auto("Toyota");
        Bicicleta b = new Bicicleta("Trek");
        a.acelerar(10); a.acelerar(5);
        b.acelerar(7);
        assertEquals(15, a.getVelocidad());
        assertEquals(7, b.getVelocidad());
        assertTrue(a.mover().contains("Auto Toyota"));
        assertTrue(b.mover().contains("Bici Trek"));
    }

    @Test
    void testFrenarNoNegativo() {
        Auto a = new Auto("Toyota");
        a.acelerar(10);
        a.frenar(15);
        assertEquals(0, a.getVelocidad());
    }

    @Test
    void testValidacionDelta() {
        Auto a = new Auto("Toyota");
        assertThrows(IllegalArgumentException.class, () -> a.acelerar(-1));
        assertThrows(IllegalArgumentException.class, () -> a.frenar(-2));
    }
}
