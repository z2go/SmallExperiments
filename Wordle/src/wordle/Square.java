package wordle;

public class Square {
    int posX;
    int posY;
    String status;
    char letter;
    public Square() {
        this.posX = 0;
        this.posY = 0;
        this.status = "NONE";
        this.letter = '.';
    }
}
