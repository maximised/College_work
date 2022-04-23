package cs3318.raytracing;

import java.awt.*;
import java.util.List;

/**
 * Sphere class gives us an example of a renderable object
 * @author Leonard McMillan
 * @since 1998
 */
final class Sphere implements Renderable {
    private final Surface surface;
    private final Vector3D center;
    private final float radius;
    private final float radSqr;

    /**
     * Sphere consists of surface, center and radius values
     * radius squared values calculated from given radius
     * @param s surface of the sphere
     * @param c center of sphere position
     * @param r radius of the sphere
     */
    public Sphere(Surface s, Vector3D c, float r) {
        surface = s;
        center = c;
        radius = r;
        radSqr = r * r;
    }

    /**
     * Check intersection components of the sphere
     * See if there is an intersection closer than previous intersection
     * See if ray intersects sphere
     * See if the intersection is in the positive ray direction
     * See it is the closest so far
     * @param ray The ray that we are checking for intersection
     * @return bool True if the ray intersects.
     */
    @Override
    public boolean intersect(Ray ray) {
        // mc: make sure to make Ray less mutable and change to setters or alternative
        float dx = center.x - ray.origin.x;
        float dy = center.y - ray.origin.y;
        float dz = center.z - ray.origin.z;
        float v = ray.direction.dot(dx, dy, dz);

        // Do the following quick check to see if there is even a chance
        // that an intersection here might be closer than a previous one
        if (v - radius > ray.getT())
            return false;

        // Test if the ray actually intersects the sphere
        float t = radSqr + v * v - dx * dx - dy * dy - dz * dz;
        if (t < 0)
            return false;


        t = v - ((float) Math.sqrt(t));
        if ((t > ray.getT()) || (t < 0))
            return false;
        ray.setT(t);
        ray.setObject(this);
        return true;
    }

    /**
     * Defines geometric information for a surface shader
     *
     * 1. the point of intersection (p)
     * 2. a unit-length surface normal (n)
     * 3. a unit-length vector towards the ray's origin (v
     *
     * We call Shade method to apply illumination model
     *
     * @param ray a ray
     * @param lights lights emitting light
     * @param objects objects casting shadows
     * @param bgnd background colour
     * @return the shade of the surface on self sphere object.
     */
    @Override
    public Color Shade(Ray ray, java.util.List<Object> lights, List<Object> objects, Color bgnd) {

        float px = ray.origin.x + ray.getT() * ray.direction.x;
        float py = ray.origin.y + ray.getT() * ray.direction.y;
        float pz = ray.origin.z + ray.getT() * ray.direction.z;

        Vector3D p = new Vector3D(px, py, pz);
        Vector3D v = new Vector3D(-ray.direction.x, -ray.direction.y, -ray.direction.z);
        Vector3D n = new Vector3D(px - center.x, py - center.y, pz - center.z);
        n.normalize();

        return surface.Shade(p, n, v, lights, objects, bgnd);
    }

    /**
     * String method
     * @return Sphere's center and radius values
     */
    @Override
    public String toString() {
        return ("sphere " + center + " " + radius);
    }
}
