package c3318.colour;

import java.util.Arrays;
import java.util.HashMap;

/**
 * Colour class creates a colour object that stores a model with component values
 * @author Maxim Chopivskyy
 * @since 2020
 */
public class Colour {
    private final int[] COMPONENT_VALUES;
    private final String COLOUR_MODEL;
    private final HashMap<Character, Integer> MODEL_VALUES_DICT;

    private final static int MIN_RANGE = 0;
    private final static int MAX_RANGE = 255;
    private final static int MODEL_LENGTH = 3;

    /**
     * Creates the colour object with the model and component values.
     * The component values are stored in a list.
     * A dictionary mapping the model to the values is also stored.
     * Valid component values are ints between 0 and 255.
     * @param colour_model The model of the colour. Default is RGB
     * @param c1 component value 1
     * @param c2 component value 2
     * @param c3 component value 3
     */
    public Colour(String colour_model, int c1, int c2, int c3) {
        COMPONENT_VALUES = new int[]{c1,c2,c3};
        exceptionIfModelNotRightLength(colour_model);
        exceptionIfAnyValuesOutOfRange(COMPONENT_VALUES);
        exceptionIfCharacterInModelRepeated(colour_model);

        COLOUR_MODEL = colour_model;

        MODEL_VALUES_DICT = new HashMap<>() {{
            for(
                int i = 0; i<MODEL_LENGTH; i++) {
                    put(COLOUR_MODEL.charAt(i), COMPONENT_VALUES[i]);
                }
        }};
    }

    /**
     * Creates colour object with default model RGB.
     * @param c1 component value 1
     * @param c2 component value 2
     * @param c3 component value 3
     */
    public Colour(int c1, int c2, int c3) {
        this("RGB", c1, c2, c3);
    }

    /**
     * returns the component value of a given component model charaacter
     * @param component the model component
     * @return the component value
     */
    public int getComponentValue(Character component) {
        return MODEL_VALUES_DICT.get(component);
    }

    /**
     * returns all the component values
     * @return the component values
     */
    public int[] getCOMPONENT_VALUES() {
        return COMPONENT_VALUES;
    }

    /**
     * returns the colour model
     * @return the colour model
     */
    public String getCOLOUR_MODEL() {
        return COLOUR_MODEL;
    }

    /**
     * given a colour model, determines if the model is the right length and throes an exception if
     * the model is not right length
     * @param colour_model the colour model
     */
    private static void exceptionIfModelNotRightLength(String colour_model) {
        if (colour_model.length() != MODEL_LENGTH) {
            throw new IllegalArgumentException("Model length should be length three.");
        }
    }

    /**
     * given the component values, determines if any of the values are out of range and throws an exception if any are.
     * @param component_values the component values
     */
    private static void exceptionIfAnyValuesOutOfRange(int[] component_values) {
        if(Arrays.stream(component_values).anyMatch(value -> value<MIN_RANGE || value>MAX_RANGE)) {
            throw new IllegalArgumentException("Each component value should be between 0 and 255.");
        }
    }

    /**
     * given the colour model, determines if a character is repeated and throws an exception if there is.
     * This is done so we can have a map of model and values
     * @param model the colour model
     */
    private static void exceptionIfCharacterInModelRepeated(String model) {
        if ( Arrays.stream(model.split("")).anyMatch(c -> (model.length() - model.replaceAll(c, "").length()) > 1 ) ) {
            throw new IllegalArgumentException("Each character in the model should be unique.");
        }
    }

    /**
     * Compares the this colour object with a given colour object.
     * True is only returned if the other object is a Colour object with the same model and values.
     * @param obj other object to be compared
     * @return False if other object is not a Colour object or doesn't have the same model and component values. True if the object is Colour with same model and values.
     */
    @Override
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }

        if (obj.getClass() != this.getClass()) {
            return false;
        }

        final Colour other = (Colour) obj;
        return  ( (this.getCOLOUR_MODEL().equals(other.getCOLOUR_MODEL()) && Arrays.equals(this.getCOMPONENT_VALUES(), other.getCOMPONENT_VALUES())) );
    }

    /**
     * returns a colour object with the values added between this colour object and a given colour object.
     * An exception is thrown if the models are different.
     * There is cap of 255 for the values, meaning sums over 255 will set as 255.
     * @param other given Colour object
     * @return Colour object with sum of values between this and given Colour object.
     */
    public Colour add(Colour other) {
        if (!this.getCOLOUR_MODEL().equals(other.getCOLOUR_MODEL())) {
            throw new IllegalArgumentException("Models should be the same in both colours.");
        }

        int[] values = new int[MODEL_LENGTH];
        for (int i=0; i<this.getCOMPONENT_VALUES().length; i++) {
            values[i] = Math.min(MAX_RANGE, this.getCOMPONENT_VALUES()[i] + other.getCOMPONENT_VALUES()[i]);
        }
        int c1 = values[0];
        int c2 = values[1];
        int c3 = values[2];

        return new Colour(this.COLOUR_MODEL, c1, c2, c3);
    }
}
