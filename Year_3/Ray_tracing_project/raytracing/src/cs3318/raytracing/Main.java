package cs3318.raytracing;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

/**
 * Main class launches a starting point for our program
 * It acts as our API
 * @author Leonard McMillan
 * @since 1998
 */

public class Main extends Application {

    /**
     * Initialising the scene to be rendered and runs our main program
     * @param primaryStage The primary stage
     * @throws Exception throws Exception when invalid values are passed
     */
    @Override
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader loader = new FXMLLoader(getClass().getResource("render.fxml"));
        //Parent root = loader.load(getClass().getResource("render.fxml").openStream());
        Parent root = loader.load();
        Controller controller = (Controller) loader.getController();

        primaryStage.setTitle("Simple Ray Tracing");
        primaryStage.setScene(new Scene(root, 860, 640));
        //

        //controller.setStage(primaryStage);
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
