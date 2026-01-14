package org.pilha;
import java.util.EmptyStackException;

public interface IPilha<T> {

    //adicionar 
    void adicionar(T elemento);

    //remover (assumindo que do topo)
    T remover();

    //pegar ou consultar o topo
    T topo();

    //tamanho
    int tamanho();

    //vazia ? 
    boolean vazia();

}