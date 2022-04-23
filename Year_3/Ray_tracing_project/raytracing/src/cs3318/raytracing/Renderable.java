package cs3318.raytracing;

import java.awt.*;
import java.util.List;

/**
 * Renderable interface used to implement ray tracing
 * Interface makes it easier to add new objects
 * Objects must implement a renderable interface to be ray traced
 */

abstract interface Renderable {
    abstract boolean intersect(Ray r);

    abstract Color Shade(Ray r, java.util.List<Object> lights, List<Object> objects, Color bgnd);

    String toString();
}
