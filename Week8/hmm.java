import java.util.*;

public class Main {
    public static void main(String[] args) {

        String[] states = {"Rainy", "Sunny"};
        String[] obs = {"walk", "shop", "clean"};

        Map<String, Double> start = Map.of("Rainy", 0.6, "Sunny", 0.4);

        Map<String, Map<String, Double>> trans = Map.of(
            "Rainy", Map.of("Rainy", 0.7, "Sunny", 0.3),
            "Sunny", Map.of("Rainy", 0.4, "Sunny", 0.6)
        );

        Map<String, Map<String, Double>> emit = Map.of(
            "Rainy", Map.of("walk", 0.1, "shop", 0.4, "clean", 0.5),
            "Sunny", Map.of("walk", 0.6, "shop", 0.3, "clean", 0.1)
        );

        System.out.println(forward(states, obs, start, trans, emit));
    }

    static double forward(String[] states, String[] obs,
                          Map<String, Double> start,
                          Map<String, Map<String, Double>> trans,
                          Map<String, Map<String, Double>> emit) {

        Map<String, Double> prev = new HashMap<>();

        
        for (String s : states)
            prev.put(s, start.get(s) * emit.get(s).get(obs[0]));

        
        for (int t = 1; t < obs.length; t++) {
            Map<String, Double> curr = new HashMap<>();
            for (String cs : states) {
                double sum = 0;
                for (String ps : states)
                    sum += prev.get(ps) * trans.get(ps).get(cs);
                curr.put(cs, sum * emit.get(cs).get(obs[t]));
            }
            prev = curr;
        }

        // Termination
        double total = 0;
        for (double v : prev.values()) total += v;
        return total;
    }
}