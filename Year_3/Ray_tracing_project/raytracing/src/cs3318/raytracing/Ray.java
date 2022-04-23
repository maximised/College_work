package cs3318.raytracing;

import java.awt.*;
import java.util.List;

/**
 * A ray can be defined as a part of a line that has a fixed starting point but no end point.
 * The following class is used to construct ray values to be used throughout ray tracing
 * @author Leonard McMillan
 * @since 1998
 */

/**
 * Ray
 * @author Leonard McMillan
 * @since 1998
 */
final class Ray {
    private static final float MAX_T = Float.MAX_VALUE;
    final Vector3D origin;
    final Vector3D direction;
    private float t;
    private Renderable object;

    /**
     * Defines ray values (origin and direction)
     * Normalise function is used on our direction parameter (makes it 1)
     * @param eye
     * @param dir
     */

    /**
     *
     * @param eye
     * @param dir
     */
    public Ray(Vector3D eye, Vector3D dir) {
        origin = new Vector3D(eye);
        direction = Vector3D.normalize(dir);
    }

    /**
     *
     * @param objects
     * @return
     */
    public boolean trace(List<Object> objects) {
        setT(MAX_T);
        //object = null;
        for (Object objList : objects) {
            Renderable object = (Renderable) objList;
            object.intersect(this);
        }
        return (object != null);
    }

    // The following method is not strictly needed, and most likely
    // adds unnecessary overhead, but I prefered the syntax
    //
    //            ray.Shade(...)
    // to
    //            ray.object.Shade(ray, ...)
    //
    // maxim here: I was suspicious of below method, but its probably ok the way it is,
    // as it seems to follow the point of composition well

    /**
     * Gets shade values from the object which is passed in
     * @param lights
     * @param objects
     * @param bgnd
     * @return Shade value of object
     */
    public final Color Shade(List<Object> lights, List<Object> objects, Color bgnd) {
        return object.Shade(this, lights, objects, bgnd);
    }

    /**
     * String method
     * @return Rays origin, direction, and t value
     */

    @Override
    public String toString() {
        return ("ray origin = " + origin + "  direction = " + direction + "  t = " + getT());
    }

    /**
     * Getter to access ray's t value
     * @return t value
     */

    public float getT() {
        return t;
    }

    /**
     * Setter to access ray's t value
     * @param t
     */

    public void setT(float t) {
        this.t = t;
    }

    /**
     * Use renderable interface to get object
     * @return object
     */

    public Renderable getObject() {
        return object;
    }

    /**
     * Use renderable interface to set object
     * @param object
     */

    public void setObject(Renderable object) {
        this.object = object;
    }
}
