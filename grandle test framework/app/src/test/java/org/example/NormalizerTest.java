/*
package org.example;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class NormalizerTest {

    @Test
    void normalizaTexto() {
        String input = "Ruan Rickelme";
        String expected = "ruan_rickelme";
        String observer = Normalizer.normalize(input);
        assertEquals(expected, observer);
    }

    @Test
    void normalizaTextoComMuitosEspacos() {
        String input = "Ruan     Rickelme";
        String expected = "ruan_rickelme";
        String observer = Normalizer.normalize(input);
        assertEquals(expected, observer);
    }

    @Test
    void normalizaTextoComMuitosInicioFim() {
        String input = "  Ruan Rickelme   ";
        String expected = "ruan_rickelme";
        String observer = Normalizer.normalize(input);
        assertEquals(expected, observer);
    }

    @Test
    void normalizaTextoComUnderlineInicioFim() {
        String input = "_Ruan Rickelme_";
        String expected = "ruan_rickelme";
        String observer = Normalizer.normalize(input);
        assertEquals(expected, observer);
    }

    @Test
    void normalizeNull(){
        String input = null;
        assertThrows(
            IllegalArgumentException.class, () -> {
                Normalizer.normalize(input);
            }
        );
    }
}


*/