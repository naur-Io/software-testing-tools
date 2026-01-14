package org.example;



public class Normalizer {
    private Normalizer(){}

    public static String normalize(String input){
        if(input == null){
            throw new IllegalArgumentException("Input nulo");
        }
        String normalized = input.trim().toLowerCase().replaceAll("_", " ");
        normalized = normalized.replaceAll("\\s+", " ");
        normalized = normalized.replaceAll(" ", "_");
        return normalized;
    }
}