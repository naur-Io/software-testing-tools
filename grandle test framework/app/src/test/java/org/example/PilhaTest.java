/*
package org.example;

import org.pilha.IPilha;
import org.junit.jupiter.api.Test;
import java.util.EmptyStackException;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.*;

public class PilhaTest {
    private IPilha<Integer> pilha;

    @BeforeEach
    void setup() {
        
    }

    @Test
    void pilhaNovaSempreVazia(){
        assertTrue(pilha.vazia());
    }

    @Test
    void adicionarNuloLanceExecao(){
        assertThrows(IllegalArgumentException.class, () -> {
            pilha.adicionar(null);
        });
    }

    @Test
    void adicionarElementoAumentaTamanhoDaPilha(){
        int tamanhoIncial = pilha.tamanho();
        pilha.adicionar(1);
        assertEquals(tamanhoIncial + 1, pilha.tamanho());
    }

    @Test
    void removerElementoDePilhaVaziaLancaExecao(){
        assertThrows(EmptyStackException.class, () -> {
            pilha.remover();
        });
    }

    @Test
    void adicionarElementoNoTopo(){
        pilha.adicionar(1);
        assertEquals(1, pilha.topo());
        pilha.adicionar(2);
        assertEquals(2, pilha.topo());
    }

    @Test
    void removerElementoTopo(){
        pilha.adicionar(1);
        pilha.adicionar(2);
        int topoAntesRemover = pilha.topo();
        int removido = pilha.remover();
        assertEquals(topoAntesRemover, removido);
        assertEquals(1, pilha.topo());  
    }

    @Test
    void tamanhoDaPilha(){
        pilha.adicionar(1);
        pilha.adicionar(2);
        assertEquals(2, pilha.tamanho());
    }

    
}

*/