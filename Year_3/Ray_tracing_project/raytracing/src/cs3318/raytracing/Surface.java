package cs3318.raytracing;

import java.awt.*;
import java.util.List;

/**
 * Surface class defines values for our surface objects
 * ka =  ambient reflection coefficient
 * kd = diffuse reflection coefficient
 * ks = specular reflection coefficient
 * kt = transmission coefficient
 * kr = reflectance coefficient
 * ns phong exponent
 * @author Leonard McMillan
 * @since 1998
 */
final class Surface {
    private final float ir, ig, ib;        // surface's intrinsic color
    private final float ka, kd, ks, ns;    // constants for phong model
    private final float kt, kr, nt;
    private static final float TINY = 0.001f;
    private static final float I255 = 0.00392156f;  // 1/255

    /**
     * RGB values, dimensions, and index values defined
     * RGB values should be between 0 and 255
     * @param rval red component value
     * @param gval green component value
     * @param bval blue component value
     * @param a ambient reflection coefficient
     * @param d diffuse reflection coefficient
     * @param s specular reflection coefficient
     * @param n phong exponent
     * @param r reflectance coefficient
     * @param t transmission coefficient
     * @param index index
     */
    public Surface(float rval, float gval, float bval, float a, float d, float s, float n, float r, float t, float index) {
        ir = rval;
        ig = gval;
        ib = bval;
        ka = a;
        kd = d;
        ks = s;
        ns = n;
        kr = r * I255;
        kt = t;
        nt = index;
    }

    /**
     * Gathers appropriate shade illumination values.
     * Computes the color of the shade on self surface based on other light objects and objects.
     * Reflection, refraction and shadows are considered when computing the shade.
     *
     * @param p vector p
     * @param n vector n
     * @param v vector v
     * @param lights List of lights shining on self object.
     * @param objects objects casting shadows
     * @param bgnd background colour
     * @return The color in the shade
     */
    Color Shade(Vector3D p, Vector3D n, Vector3D v, List<Object> lights, List<Object> objects, Color bgnd) {
        float r = 0;
        float g = 0;
        float b = 0;

        float[] rgb_values = lightAndShadowRGBEffect(p, n, v, lights, objects, r, g, b);
        r = rgb_values[0];
        g = rgb_values[1];
        b = rgb_values[2];

        // Compute illumination due to reflection
        rgb_values = computeIlluminationFromReflection(p, n, v, lights, objects, bgnd, r, g, b);
        r = rgb_values[0];
        g = rgb_values[1];
        b = rgb_values[2];

        // Add code for refraction here
        r = Math.min(r, 1f);
        g = Math.min(g, 1f);
        b = Math.min(b, 1f);

        r = (r < 0) ? 0 : r;
        g = (g < 0) ? 0 : g;
        b = (b < 0) ? 0 : b;

        return new Color(r, g, b);
    }

    /**
     * Calculates rgb values based on the given lights in the parameter and the objects casting shadows on the surface.
     * Returns the resulting rgb values as a float array.
     * @param p vector p
     * @param n vector n
     * @param v vector v
     * @param lights lights being cast
     * @param objects objects for shadows
     * @param r red component value
     * @param g green component value
     * @param b blue component value
     * @return resulting rgb values
     */
    private float[] lightAndShadowRGBEffect(Vector3D p, Vector3D n, Vector3D v, List<Object> lights, List<Object> objects, float r, float g, float b) {
        for (Object lightSources : lights) {
            Light light = (Light) lightSources;
            if (light.getLightType() == Light.LightType.AMBIENT) {
                r += ka * ir * light.ir;
                g += ka * ig * light.ig;
                b += ka * ib * light.ib;
            } else {
                Vector3D l;
                if (light.getLightType() == Light.LightType.POINT) {
                    l = new Vector3D(light.getX() - p.x, light.getY() - p.y, light.getZ() - p.z);
                    l = l.normalize();
                } else {
                    l = new Vector3D(-light.getX(), -light.getY(), -light.getZ());
                }

                // Check if the surface point is in shadow
                Vector3D poffset = new Vector3D(p.x + TINY * l.x, p.y + TINY * l.y, p.z + TINY * l.z);
                Ray shadowRay = new Ray(poffset, l);
                if (shadowRay.trace(objects))
                    break;

                float lambert = Vector3D.dot(n, l);
                if (lambert > 0) {
                    if (kd > 0) {
                        float diffuse = kd * lambert;
                        r += diffuse * ir * light.ir;
                        g += diffuse * ig * light.ig;
                        b += diffuse * ib * light.ib;
                    }
                    if (ks > 0) {
                        lambert *= 2;
                        float spec = v.dot(lambert * n.x - l.x, lambert * n.y - l.y, lambert * n.z - l.z);
                        if (spec > 0) {
                            spec = ks * ((float) Math.pow(spec, ns));
                            r += spec * light.ir;
                            g += spec * light.ig;
                            b += spec * light.ib;
                        }
                    }
                }
            }
        }
        return new float[]{r, g, b};
    }

    /**
     * Computes Illumination on Surface from reflection with other objects.
     * Updates the rgb component values of the self shade surface accordingly
     * @param p vector p
     * @param n vector n
     * @param v vector v
     * @param lights lights being cast
     * @param objects objects for shadows
     * @param bgnd background colour
     * @param r red component value
     * @param g green component value
     * @param b blue component value
     * @return resulting rgb values
     */
    private float[] computeIlluminationFromReflection(Vector3D p, Vector3D n, Vector3D v, List<Object> lights, List<Object> objects, Color bgnd, float r, float g, float b) {
        if (kr > 0) {
            float t = v.dot(n);
            if (t > 0) {
                t *= 2;
                Vector3D reflect = new Vector3D(t * n.x - v.x, t * n.y - v.y, t * n.z - v.z);
                Vector3D poffset = new Vector3D(p.x + TINY * reflect.x, p.y + TINY * reflect.y, p.z + TINY * reflect.z);
                Ray reflectedRay = new Ray(poffset, reflect);
                if (reflectedRay.trace(objects)) {
                    Color rcolor = reflectedRay.Shade(lights, objects, bgnd);
                    r += kr * rcolor.getRed();
                    g += kr * rcolor.getGreen();
                    b += kr * rcolor.getBlue();
                } else {
                    r += kr * bgnd.getRed();
                    g += kr * bgnd.getGreen();
                    b += kr * bgnd.getBlue();
                }
            }
        }
        return new float[]{r,g,b};
    }
}
