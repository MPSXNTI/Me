package com.poo.vehiculos;

import java.util.*;

public class App {
    public static void main(String[] args) {
        List<Vehiculo> flota = Arrays.asList(new Auto("Toyota"), new Bicicleta("Trek"));
        flota.get(0).acelerar(50);
        flota.get(1).acelerar(20);
        for (Vehiculo v : flota) System.out.println(v.mover());
    }
}
