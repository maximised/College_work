import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
import java.lang.*;
import java.io.*;

public class GUI_App {
    JButton button1;
    JButton button2;
    JFrame frame;
    JTextArea text;
    JScrollPane scroller;

    public void go() {
        frame = new JFrame();
        button1 = new JButton( "for saving" );
        button2 = new JButton( "for bringiong saved state" );
        text = new JTextArea(10, 20);
        text.setLineWrap( true );

        MyDrawPanel panel = new MyDrawPanel();

        scroller = new JScrollPane( text );
        scroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        scroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);

        panel.add( scroller );

        button1.addActionListener( new ClickButton1() );
        button2.addActionListener( new ClickButton2() );

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add( BorderLayout.WEST, button1 );
        frame.getContentPane().add( BorderLayout.EAST, button2 );
        frame.getContentPane().add( BorderLayout.CENTER, panel );
        frame.setSize(1200, 900);
        frame.setVisible(true);
    }

    


    public static void main(String[] args) {
        GUI_App gui = new GUI_App(); 
        gui.go();
    }


    class ClickButton1 implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent event) {
            button1.setText( "i have been clicked!" );

            save( text );
        }
    }

    class ClickButton2 implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent event) {
            button2.setText( "i have been clicked!" );

            restore( text );
        }
    }

    class MyDrawPanel extends JPanel {
        public void paintComponent(Graphics g) {
            Image image = new ImageIcon("Sketchpad.png").getImage();

            g.drawImage(image,0,0,500,500,this);
        }
    }


    public void save( Object o ) {
        FileOutputStream fileStream;

        try {
            fileStream = new FileOutputStream( "TextArea.ser" );

            ObjectOutputStream os = new ObjectOutputStream( fileStream );

            os.writeObject( o );

            os.close();
        }
        catch ( FileNotFoundException e ) {
            System.err.println( "File is not found error" );
        }
        catch ( IOException e ) {
            System.err.println( "IOError happened" );
            e.printStackTrace();
        }

    }

    public void restore( Object o ) {
        FileInputStream fileStream;

        try {
            fileStream = new FileInputStream( "TextArea.ser" );

            ObjectInputStream os = new ObjectInputStream( fileStream );

            Object t = os.readObject();

            JTextArea savedtext = (JTextArea) t;

            text.setText( savedtext.getText() );

            os.close();
        }
        catch ( ClassNotFoundException e ) {
            System.err.println( "Class is not found error" );
        }
        catch ( IOException e ) {
            System.err.println( "IOError happened" );
            e.printStackTrace();
        }

    }

}


