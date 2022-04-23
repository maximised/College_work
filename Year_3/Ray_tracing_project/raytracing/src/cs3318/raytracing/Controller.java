package cs3318.raytracing;

import javafx.event.ActionEvent;
import javafx.scene.image.ImageView;
import javafx.stage.Stage;

/**
 * Controller class analyses the scene details
 * @author Leonard McMillan
 * @since 1998
 */


public class Controller {
    public ImageView renderedImage;
    private Stage stage;
    private Driver sceneToRender;
    boolean finished = false;

    /**
     * sets stage
     * @param stage The stage
     */

    public void setStage(Stage stage) {
        this.stage = stage;
    }

    /**
     * analyse scene dimensions to associate pixels
     */

    public void run() {
        long time = System.currentTimeMillis();
        for (int j = 0; j < sceneToRender.getHeight(); j += 1) {
            for (int i = 0; i < sceneToRender.getWidth(); i += 1) {
                sceneToRender.renderPixel(i, j);
            }
        }
        renderedImage.setImage(sceneToRender.getRenderedImage());
        time = System.currentTimeMillis() - time;
        System.err.println("Rendered in "+(time/60000)+":"+((time%60000)*0.001));
        finished = true;
    }

    /**
     * initialise the raytrace
     * call new driver object with dimensions
     * @param actionEvent The action Event
     */

    public void startRayTrace(ActionEvent actionEvent) {
        sceneToRender = new Driver((int) renderedImage.getFitWidth(),
                                   (int) renderedImage.getFitHeight(),
                "resources/SceneToRender.txt");
        this.run();
    }
}
