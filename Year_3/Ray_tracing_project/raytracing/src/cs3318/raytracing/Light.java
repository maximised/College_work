package cs3318.raytracing;

import java.util.Arrays;

/**
 * Light assesses light properties such as position,direction,intensity
 * Lights class and Surfaces class keep a relationship
 * @author Leonard McMillan
 * @since 1998
 */
final class Light {
    enum LightType {AMBIENT, DIRECTIONAL, POINT}

    private final LightType lightType;
    private Vector3D lvec;           // the position of a point light or
    // the direction to a directional light
    final float ir, ig, ib;        // intensity of the light source
    private static final float MIN_COMPONENT_RANGE = 0;
    private static final float MAX_COMPONENT_RANGE = 255;

    /**
     * Defines light properties according to light type, the vector, and RGB values
     *
     * Light type is returned via a getter method
     * @param type type of light (Ambient, Directional, Point)
     * @param v The vector that defines where the light is, which way it points and how intense it is.
     * @param r red component value
     * @param g green component value
     * @param b blue component value
     */
    public Light(LightType type, Vector3D v, float r, float g, float b) {
        lightType = type;
        ir = r;
        ig = g;
        ib = b;
        verifyLightValuesAreValid(ir,ig,ib);

        if ( !type.equals(LightType.AMBIENT) ) {
            lvec = v;
            if ( type.equals(LightType.DIRECTIONAL) ) {
                lvec.normalize();
            }
        }
    }

    /**
     * Getter method to access light type that was calculated
     * @return light type
     */
    LightType getLightType() {
        return lightType;
    }

    /**
     * Get self vector's x value
     * @return Vector x value
     */
    float getX() {
        return lvec.x;
    }

    /**
     * Get self vector's y value
     * @return Vector y value
     */
    float getY() {
        return lvec.y;
    }

    /**
     * Get self vector's z value
     * @return Vector's z value
     */
    float getZ() {
        return lvec.z;
    }

    /**
     * Checks if the rgb values of self light object are valid, meaning the values are between the minimum and maximum range.
     * The minimum range is 0 and maximum is 255.
     *
     * @param r red component value
     * @param g green component value
     * @param b blue component value
     */
    private static void verifyLightValuesAreValid(float r, float g, float b) {
        double[] component_values = new double[]{r, g, b};
        if(!Arrays.stream(component_values).allMatch(value -> value>=MIN_COMPONENT_RANGE && value<=MAX_COMPONENT_RANGE)) {
            throw new IllegalArgumentException("Each light component value should be between 0 and 255.");
        }
    }
}
