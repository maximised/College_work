package cs3318.raytracing;


/**
 * Vector3D class represents a point in a 3 dimensional plane
 * Vectors are immutable and cannot be inherited from.
 */
final class Vector3D {
    final float x,y,z;

    /**
     * Constructs and initialised a vector in a 3D space on default position (0,0,0).
     * Used when no x,y,z parameters are supplied.
     */
    public Vector3D( ) {
        // made x,y,z final for less mutability
        this(0,0,0);
    }

    /**
     * Constructs and initialised a vector in a 3D space on position (x,y,z)
     * All dimensions of the vector can be any real number.
     * @param x The x dimension
     * @param y The y dimension
     * @param z the z dimension
     */
    public Vector3D(float x, float y, float z) {
        this.x = x; this.y = y; this.z = z;
    }

    /**
     * Establish a vector and assign it (x,y,z) co-ordinates
     * @param v The vector we use the x,y,z values from to construct the current Vector object
     */
    public Vector3D(Vector3D v) {
        this(v.x,v.y,v.z);
    }

    /**
     * Calculates the dot product of self and vector supplied in parameter.
     * @param B vector B
     * @return The dot product of self and vector B
     */
    public final float dot(Vector3D B) {
        return dot(B.x,B.y,B.z);
    }

    /**
     * Calculates the dot product of self and vector supplied in parameter.
     * vector B is supplied by its individual x,y,z values
     * @param Bx x dimension value of vector B
     * @param By y dimension value of vector B
     * @param Bz z dimension value of vector B
     * @return The dot product of self and vector B
     */
    public final float dot(float Bx, float By, float Bz) {
        return (x*Bx + y*By + z*Bz);
    }

    /**
     * Perform dot method on Vector A and Vector B
     * @param A vector A
     * @param B vector B
     * @return The dot product of vector A and vector B
     */
    public static final float dot(Vector3D A, Vector3D B) {
        //return (A.x*B.x + A.y*B.y + A.z*B.z);
        return A.dot(B);
    }

    /**
     * The cross method ultimately finds the cross product of 2 vectors
     * The cross product is returned.
     * @param B The second vector that we cross product with the current vector
     * @return The cross product of the two vectors
     */
    public final Vector3D cross(Vector3D B) {
        return cross(B.x,B.y,B.z);
    }

    /**
     * Returns a vector that results from the cross product of this object and the other vector object supplied in the parameter.
     * The other vector is supplied by the individual x,y,z values.
     * x, y, z can be any real number.
     * @param Bx x dimension of the second parameter
     * @param By y dimension of the second parameter
     * @param Bz z dimension of the second parameter
     * @return The cross product of the two vectors
     */
    public final Vector3D cross(float Bx, float By, float Bz) {
        return new Vector3D(y*Bz - z*By, z*Bx - x*Bz, x*By - y*Bx);
    }

    /**
     * Finds cross product of Vector A and Vector B
     * @param A vector A
     * @param B vector B
     * @return The cross product of the two vectors
     */
    public final static Vector3D cross(Vector3D A, Vector3D B) {
        //return new Vector3D(A.y*B.z - A.z*B.y, A.z*B.x - A.x*B.z, A.x*B.y - A.y*B.x);
        return A.cross(B);
    }

    /**
     * Establish a length function to assess vector length of self vector object.
     * @return length of the vector
     */
    public final float length() {
        return length(this);
    }

    /**
     * Find length of a given vector
     * @param A vector that we find the length of
     * @return Vector length of vector A
     */
    public final static float length(Vector3D A) {
        return (float) Math.sqrt(A.x*A.x + A.y*A.y + A.z*A.z);
    }

    /**
     * Normalise function makes self vector object length = 1
     * @return The normalised vector of self object
     */
    final Vector3D normalize( ) {
        return normalize(this);
    }

    /**
     * Using normalise function on the Vector passed in
     * @param A vector A
     * @return The normalised vector of A
     */
    final static Vector3D normalize(Vector3D A) {
        float t = A.x*A.x + A.y*A.y + A.z*A.z;
        if (t != 0 && t != 1) t = (float)(1 / Math.sqrt(t));
        return new Vector3D(A.x*t, A.y*t, A.z*t);
    }

    /**
     * Prints out the vector x,y,z values of self.
     * @return (x,y,z) vector values
     */
    @Override
    public String toString() {
        return "[" + x + ", " + y + ", " + z + "]";
    }
}


