
//1. Java Program Structure – Arithmetic & Logical Operations
public class BasicJava {
    public static void main(String[] args) {
// Arithmetic Operations
        int a = 10, b = 5;
        System.out.println("Addition : " + (a + b));
        System.out.println("Subtraction : " + (a - b));
        System.out.println("Multiplication: " + (a * b));
        System.out.println("Division : " + (a / b));
        System.out.println("Modulus : " + (a % b));
// Logical Operations
        boolean x = true, y = false;
        System.out.println("AND : " + (x && y));
        System.out.println("OR : " + (x || y));
        System.out.println("NOT : " + (!x));
    }
}
//2. String Operations using String and StringBuffer
public class StringOps {
    public static void main(String[] args) {
// String class operations
        String s = "Hello World";
        System.out.println("Length : " + s.length());
        System.out.println("Uppercase : " + s.toUpperCase());
        System.out.println("Lowercase : " + s.toLowerCase());
        System.out.println("Substring : " + s.substring(6));
        System.out.println("Replace : " + s.replace("World", "Java"));
        System.out.println("Contains 'lo': " + s.contains("lo"));
// StringBuffer operations
        StringBuffer sb = new StringBuffer("Java");
        sb.append(" Programming");
        System.out.println("After Append : " + sb);
        sb.insert(4, " is Fun");
        System.out.println("After Insert : " + sb);
        sb.reverse();
        System.out.println("After Reverse: " + sb);
    }
}
//3. Inner Class and Static Fields
public class OuterClass {
    // Static field - shared by all objects
    static int staticCount = 0;
    int id;
    OuterClass(int id) {
        this.id = id;
        staticCount++;
    }
    // Inner class
    class InnerClass {
        void show() {
            System.out.println("Inner class accessed from Outer ID: " + id);
        }
    }
    public static void main(String[] args) {
        OuterClass obj1 = new OuterClass(1);
        OuterClass obj2 = new OuterClass(2);
        System.out.println("Static Count: " + staticCount);
// Creating inner class object
        OuterClass.InnerClass inner = obj1.new InnerClass();
        inner.show();
    }
}
//4. Inheritance and Polymorphism
// Parent class
class Animal {
    String name;
    Animal(String name) {
        this.name = name;
    }
    void sound() {
        System.out.println(name + " makes a sound");
    }
}
// Child class - Inheritance
class Dog extends Animal {
    Dog(String name) {
        super(name); // calling parent constructor
    }
    // Polymorphism - method overriding
    @Override
    void sound() {
        System.out.println(name + " says: Woof!");
    }
}
class Cat extends Animal {
    Cat(String name) {
        super(name);
    }
    @Override
    void sound() {
        System.out.println(name + " says: Meow!");
    }
}
public class InheritanceDemo {
    public static void main(String[] args) {
        Animal a = new Animal("Animal");
        Animal d = new Dog("Dog"); // Polymorphism
        Animal c = new Cat("Cat");
        a.sound();
        d.sound();
        c.sound();
    }
}
//5. 2D Shapes on Frames (AWT)
import java.awt.*;
public class ShapesFrame extends Frame {
    public void paint(Graphics g) {
// Draw Line
        g.setColor(Color.RED);
        g.drawLine(50, 50, 200, 50);
// Draw Rectangle
        g.setColor(Color.BLUE);
        g.drawRect(50, 80, 150, 80);
// Draw Filled Oval
        g.setColor(Color.GREEN);
        g.fillOval(50, 200, 150, 80);
// Draw Arc
        g.setColor(Color.ORANGE);
        g.drawArc(50, 310, 150, 80, 0, 180);
    }
    public static void main(String[] args) {
        ShapesFrame f = new ShapesFrame();
        f.setTitle("2D Shapes");
        f.setSize(300, 450);
        f.setVisible(true);
    }
}
//6. Color and Fonts
import java.awt.*;
public class ColorFontDemo extends Frame {
    public void paint(Graphics g) {
// Set Font and draw text
        g.setFont(new Font("Arial", Font.BOLD, 24));
        g.setColor(Color.BLUE);
        g.drawString("Bold Blue Text", 50, 80);
        g.setFont(new Font("Times New Roman", Font.ITALIC, 20));
        g.setColor(Color.RED);
        g.drawString("Italic Red Text", 50, 130);
        g.setFont(new Font("Courier", Font.PLAIN, 18));
        g.setColor(Color.MAGENTA);
        g.drawString("Plain Magenta Text", 50, 180);
// Colored filled shapes
        g.setColor(new Color(255, 165, 0)); // Custom orange
        g.fillRect(50, 210, 200, 50);
    }
    public static void main(String[] args) {
        ColorFontDemo f = new ColorFontDemo();
        f.setTitle("Color and Font Demo");
        f.setSize(350, 320);
        f.setVisible(true);
    }
}
//7. Various Swing Components
import javax.swing.*;
        import java.awt.*;
public class SwingComponents extends JFrame {
    SwingComponents() {
        setLayout(new FlowLayout());
// Label
        add(new JLabel("Enter Name:"));
// TextField
        add(new JTextField(10));
// Button
        add(new JButton("Click Me"));
// Checkbox
        add(new JCheckBox("Accept Terms"));
// Radio Buttons
        JRadioButton r1 = new JRadioButton("Male");
        JRadioButton r2 = new JRadioButton("Female");
        ButtonGroup bg = new ButtonGroup();
        bg.add(r1); bg.add(r2);
        add(r1); add(r2);
// ComboBox (Dropdown)
        String[] items = {"Java", "Python", "C++"};
        add(new JComboBox<>(items));
        setTitle("Swing Components");
        setSize(300, 250);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }
    public static void main(String[] args) {
        new SwingComponents();
    }
}
//8. Dialog Box and Menus
import javax.swing.*;
        import java.awt.event.*;
public class DialogMenuDemo extends JFrame implements ActionListener {
    DialogMenuDemo() {
// Create Menu Bar
        JMenuBar mb = new JMenuBar();
// File Menu
        JMenu fileMenu = new JMenu("File");
        JMenuItem newItem = new JMenuItem("New");
        JMenuItem exitItem = new JMenuItem("Exit");
        newItem.addActionListener(this);
        exitItem.addActionListener(this);
        fileMenu.add(newItem);
        fileMenu.add(exitItem);
        mb.add(fileMenu);
        setJMenuBar(mb);
        setTitle("Dialog and Menu Demo");
        setSize(400, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent e) {
        String cmd = e.getActionCommand();
        if (cmd.equals("New")) {
            JOptionPane.showMessageDialog(this, "New File Created!");
        } else if (cmd.equals("Exit")) {
            int choice = JOptionPane.showConfirmDialog(this, "Exit?");
            if (choice == JOptionPane.YES_OPTION) System.exit(0);
        }
    }
    public static void main(String[] args) {
        new DialogMenuDemo();
    }
}
//9. Event Handling
import javax.swing.*;
        import java.awt.*;
        import java.awt.event.*;
public class EventHandling extends JFrame
        implements ActionListener, MouseListener, KeyListener {
    JLabel label;
    EventHandling() {
        label = new JLabel("Events will show here", JLabel.CENTER);
        JButton btn = new JButton("Click Me");
        btn.addActionListener(this); // Button event
        addMouseListener(this); // Mouse event
        addKeyListener(this); // Key event
        setFocusable(true);
        setLayout(new BorderLayout());
        add(btn, BorderLayout.NORTH);
        add(label, BorderLayout.CENTER);
        setTitle("Event Handling");
        setSize(400, 200);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }
    public void actionPerformed(ActionEvent e) { label.setText("Button Clicked!"); }
    public void mouseClicked(MouseEvent e) { label.setText("Mouse Clicked at: " +
            e.getX() + ", " + e.getY()); }
    public void keyPressed(KeyEvent e) { label.setText("Key Pressed: " +
            e.getKeyChar()); }
    // Unused interface methods
    public void mouseEntered(MouseEvent e) {}
    public void mouseExited(MouseEvent e) {}
    public void mousePressed(MouseEvent e) {}
    public void mouseReleased(MouseEvent e) {}
    public void keyReleased(KeyEvent e) {}
    public void keyTyped(KeyEvent e) {}
    public static void main(String[] args) { new EventHandling(); }
}
//10. Multithreading
class MyThread extends Thread {
    String name;
    int count;
    MyThread(String name, int count) {
        this.name = name;
        this.count = count;
    }
    public void run() {
        for (int i = 1; i <= count; i++) {
            System.out.println(name + " - Count: " + i);
            try {
                Thread.sleep(500); // Wait 0.5 seconds
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
    }
}
public class MultithreadDemo {
    public static void main(String[] args) {
        MyThread t1 = new MyThread("Thread-1", 3);
        MyThread t2 = new MyThread("Thread-2", 3);
        t1.start(); // Start thread 1
        t2.start(); // Start thread 2 (runs simultaneously)
    }
}
//11. Exception Handling
public class ExceptionDemo {
    public static void main(String[] args) {
// Arithmetic Exception (divide by zero)
        try {
            int a = 10, b = 0;
            int result = a / b;
            System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException: " + e.getMessage());
        }
// Array Index Out of Bounds
        try {
            int[] arr = {1, 2, 3};
            System.out.println(arr[5]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayException: " + e.getMessage());
        }
// Number Format Exception
        try {
            int x = Integer.parseInt("abc");
        } catch (NumberFormatException e) {
            System.out.println("NumberFormatException: " + e.getMessage());
        }
// Finally always runs
        try {
            System.out.println("Try block");
        } finally {
            System.out.println("Finally block always runs");
        }
    }
}
//12. File Class Operations
import java.io.*;
public class FileDemo {
    public static void main(String[] args) {
// ---- Write to File ----
        try {
            FileWriter fw = new FileWriter("demo.txt");
            fw.write("Hello, this is a Java file demo!\n");
            fw.write("Second line of the file.");
            fw.close();
            System.out.println("File written successfully.");
        } catch (IOException e) {
            System.out.println("Write Error: " + e.getMessage());
        }
// ---- Read from File ----
        try {
            BufferedReader br = new BufferedReader(new FileReader("demo.txt"));
            String line;
            System.out.println("File Content:");
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
            br.close();
        } catch (IOException e) {
            System.out.println("Read Error: " + e.getMessage());
        }
// ---- File Info ----
        File f = new File("demo.txt");
        System.out.println("File Name : " + f.getName());
        System.out.println("File Size : " + f.length() + " bytes");
        System.out.println("File Exists: " + f.exists());
    }
}
//13. JDBC – Database Connection
import java.sql.*;
public class JDBCDemo {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/testdb";
        String user = "root";
        String pass = "password";
        try {
// Step 1: Load Driver
            Class.forName("com.mysql.cj.jdbc.Driver");
// Step 2: Create Connection
            Connection con = DriverManager.getConnection(url, user, pass);
            System.out.println("Connected to Database!");
// Step 3: Create Statement
            Statement stmt = con.createStatement();
// Step 4: Execute Query
            String sql = "SELECT * FROM students";
            ResultSet rs = stmt.executeQuery(sql);
// Step 5: Display Results
            System.out.println("ID | Name | Marks");
            System.out.println("---+-------+------");
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " | " +
                        rs.getString("name") + " | " +
                        rs.getInt("marks"));
            }
// Step 6: Close Connection
            con.close();
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
/* SQL to create table:
CREATE TABLE students (
id INT PRIMARY KEY,
name VARCHAR(50),
marks INT
);
INSERT INTO students VALUES (1,'Alice',90),(2,'Bob',85);
*/
//14. Package Creation and Use
// ---- File: mypackage/Calculator.java ----
package mypackage;
public class Calculator {
    public int add(int a, int b) { return a + b; }
    public int subtract(int a, int b) { return a - b; }
    public int multiply(int a, int b) { return a * b; }
    public double divide(int a, int b) {
        if (b == 0) {
            System.out.println("Cannot divide by zero!");
            return 0;
        }
        return (double) a / b;
    }
}
// ---- File: MainApp.java ----
import mypackage.Calculator; // Import the package
public class MainApp {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println("Add : " + calc.add(10, 5));
        System.out.println("Subtract : " + calc.subtract(10, 5));
        System.out.println("Multiply : " + calc.multiply(10, 5));
        System.out.println("Divide : " + calc.divide(10, 5));
    }
}
/* Compile & Run:
javac mypackage/Calculator.java
javac MainApp.java
java MainApp
*/
