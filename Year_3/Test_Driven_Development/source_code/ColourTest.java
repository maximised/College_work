package c3318.colour;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.*;

class ColourTest {

    @Test
    public void checkIfComponentValuesAreCorrect_DefaultRGB() {
        int c1 = 12; int c2 = 0; int c3 = 200;
        Colour colour = new Colour(c1, c2, c3);
        assertEquals(12, colour.getComponentValue('R') );
        assertEquals(0, colour.getComponentValue('G') );
        assertEquals(200, colour.getComponentValue('B') );
    }

    @Test
    public void checkIfComponentValuesAreCorrect_SpecifiedModel() {
        String model = "BGb";
        int c1 = 12; int c2 = 0; int c3 = 13;
        Colour colour = new Colour(model, c1, c2, c3);
        assertEquals(13, colour.getComponentValue('b'));
    }

    @Test
    public void throwExceptionIfModelIsLongerThanThree_SpecifiedModel() {
        String model = "BGSD";
        int c1 = 12; int c2 = 0; int c3 = 200;

        Throwable exception = assertThrows(IllegalArgumentException.class, () -> new Colour(model, c1, c2, c3));
        assertEquals("Model length should be length three.", exception.getMessage());
    }

    @Test
    public void throwExceptionIfModelIsShorterThanThree_SpecifiedModel() {
        String model = "KI";
        int c1 = 12; int c2 = 0; int c3 = 200;

        Throwable exception = assertThrows(IllegalArgumentException.class, () -> new Colour(model, c1, c2, c3));
        assertEquals("Model length should be length three.", exception.getMessage());
    }

    @Test
    public void doNotThrowExceptionWhenModelIsLengthThree_SpecifiedModel() {
        String model = "ABC";
        int c1 = 12; int c2 = 0; int c3 = 200;

        assertDoesNotThrow(() -> new Colour(model, c1, c2, c3));
    }


    static Stream<Arguments> testCases() {
        return Stream.of(
                Arguments.of("ABC", 0, 12, 256),
                Arguments.of("gfd", 1, -1, 0),
                Arguments.of("ASD", -1, 256, 1000)
        );
    }
    @ParameterizedTest
    @MethodSource("testCases")
    public void throwExceptionIfComponentValuesDoNotSatisfyRange_SpecifiedModel(String model, int c1, int c2, int c3) {
        Throwable exception = assertThrows(IllegalArgumentException.class, () -> new Colour(model, c1, c2, c3));
        assertEquals("Each component value should be between 0 and 255.", exception.getMessage());
    }

    @Test
    public void doNotThrowExceptionWhenValuesSatisfyRange_SpecifiedModel(){
        String model = "ABC";
        int c1 = 12; int c2 = 0; int c3 = 255;

        assertDoesNotThrow( () -> new Colour(model, c1, c2, c3) );
    }

    @Test
    public void throwExceptionWhenCharacterIsRepeatedInModel_SpecifiedModel() {
        String model = "AbA";
        int c1 = 12; int c2 = 0; int c3 = 200;

        Throwable exception = assertThrows(IllegalArgumentException.class, () -> new Colour(model, c1, c2, c3));
        assertEquals("Each character in the model should be unique.", exception.getMessage());

    }

    @Test
    public void doNotThrowExceptionWhenEveryCharacterIsUniqueInModel_SpecifiedModel() {
        String model = "WwA";
        int c1 = 12; int c2 = 0; int c3 = 200;

        assertDoesNotThrow( () -> new Colour(model, c1, c2, c3) );
    }

    @Test
    public void ifColour1AndColour2HaveSameModelAndValuesEqualsMethodReturnsTrue_SpecifiedModel() {
        String model = "QWE";
        int c1 = 12; int c2 = 0; int c3 = 200;
        Colour colour1 = new Colour(model, c1, c2, c3);
        Colour colour2 = new Colour(model, c1, c2, c3);

        assertEquals(colour1, colour2);
    }

    @Test
    public void ifColour1AndColour2HaveDifferentModelsEqualsMethodReturnsFalse_SpecifiedModel() {
        String model1 = "QWE";
        String model2 = "qwe";
        int c1 = 12; int c2 = 0; int c3 = 200;
        Colour colour1 = new Colour(model1, c1, c2, c3);
        Colour colour2 = new Colour(model2, c1, c2, c3);

        assertNotEquals(colour1, colour2);
    }

    @Test
    public void ifColour1AndColour2HaveDifferentValuesEqualsMethodReturnsFalse_SpecifiedModel() {
        String model = "QWE";
        int c1 = 12; int c2 = 0; int c3 = 200;
        int c4 = 12; int c5 = 1; int c6 = 200;
        Colour colour1 = new Colour(model, c1, c2, c3);
        Colour colour2 = new Colour(model, c4, c5, c6);

        assertNotEquals(colour1, colour2);
    }

    @Test
    public void addMethodShouldResultInColourObjectWithValuesTheSumOfTwoOriginalColourObjects_SpecifiedModel_ValuesUnder255() {
        String model = "QWE";
        int c1 = 12; int c2 = 0; int c3 = 200;
        int c4 = 12; int c5 = 1; int c6 = 55;
        Colour colour1 = new Colour(model, c1, c2, c3);
        Colour colour2 = new Colour(model, c4, c5, c6);

        Colour expected_colour = new Colour(model, c1+c4, c2+c5, c3+c6);

        assertEquals(expected_colour, colour1.add(colour2));
    }

    @Test
    public void addMethodShouldResultInColourObjectWithValuesTheSumOfTwoOriginalColourObjects_SpecifiedModel_ValuesOver255() {
        String model = "QWE";
        int c1 = 12; int c2 = 21; int c3 = 200;
        int c4 = 12; int c5 = 255; int c6 = 56;
        Colour colour1 = new Colour(model, c1, c2, c3);
        Colour colour2 = new Colour(model, c4, c5, c6);

        Colour expected_colour = new Colour(model, 24, 255, 255);

        assertDoesNotThrow( () -> colour1.add(colour2) );
        assertEquals(expected_colour, colour1.add(colour2));
    }

    @Test
    public void throwExceptionWhenAttemptingToAddColoursWithDifferentModels_SpecifiedModel() {
        String model1 = "Acs";
        String model2 = "Rat";

        int c1 = 12; int c2 = 0; int c3 = 200;
        int c4 = 12; int c5 = 1; int c6 = 55;
        Colour colour1 = new Colour(model1, c1, c2, c3);
        Colour colour2 = new Colour(model2, c4, c5, c6);

        Throwable exception = assertThrows(IllegalArgumentException.class, () -> colour1.add(colour2));
        assertEquals("Models should be the same in both colours.", exception.getMessage());
    }
}