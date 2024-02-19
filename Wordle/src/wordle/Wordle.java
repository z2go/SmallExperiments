package wordle;
import processing.core.PApplet;
import processing.core.PFont;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Scanner;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.stream.Stream;

import java.util.Random;

public class Wordle extends PApplet{
    Scanner scanner=new Scanner("allWords.txt");
    Random random = new Random();
    float avgScore;
    int gameNum = 1;
    PFont font;
    String answer;
    int currentNum = 0;
    int guessNum = 0;
    boolean invalid = false;
    String currentGuess = "";
    int screenSizeX = 600;
    int screenSizeY = 750;
    int squareSize = 70;
    int borderSize = 2;
    Square[][] squares = new Square[7][6];
    GameState currentGameState = GameState.RUNNING;
    enum GameState{
        RUNNING,FINISHED
    }
    public static void main(String[] args) {
        PApplet.main("wordle.Wordle");

    }
    public static boolean isInFile(String book) throws IOException {
        try (FileReader fileInvc = new FileReader("allWords.txt");
             BufferedReader readervc = new BufferedReader(fileInvc)) {
            String readvc = readervc.readLine();
            while (readvc != null) {
                if (readvc.contains(book)) {
                    return true;
                }
                readvc = readervc.readLine();
            }
            return false;
        }
    }
    public void settings(){
        size(screenSizeX,screenSizeY);
    }
    public void setup(){
        answer = readFile(random.nextInt(2135)+1);
        font = createFont("helveticaneue.ttf", 128);
        textFont(font);
        for (int i = 0; i<=5; i++){
            for (int j = 0; j<=4; j++){
                squares[i][j] = new Square();
                squares[i][j].posY = i*100 + 900;
                squares[i][j].posX = j*100 + 100;
            }
        }
    }
    public void draw(){
        switch (currentGameState){
            case RUNNING -> {
                drawBackground();
                drawSquares();
            }
            case FINISHED -> {

            }
        }

    }
    public void drawBackground(){
        fill(255,255,255);
        rect(-1,-1,screenSizeX+1,screenSizeY+1);
        fill(0,0,0);
        textSize(100);
        textAlign(CENTER);
        text("HURDLE",300,100);
        if (invalid){
            textSize(30);
            fill(255,0,0);
            text("NOT A VALID WORD",300,135);
        }
    }
    public void drawSquares() {
        for (int i = 0; i <= 5; i++) {
            for (int j = 0; j <= 4; j++) {

                switch (squares[i][j].status){
                    case "NONE":
                        fill(255,255,255);
                        break;
                    case "GRAY":
                        fill(150,150,150);
                        break;
                    case "GREEN":
                        fill(0,150,0);
                        break;
                    case "YELLOW":
                        fill(150,150,0);
                        break;
                }
                rect(squares[i][j].posX - squareSize/2 - borderSize,squares[i][j].posY - screenSizeY - borderSize,squareSize+borderSize,squareSize+borderSize);
                rect(squares[i][j].posX - squareSize/2,squares[i][j].posY - squareSize/2,squareSize,squareSize);
                fill(0,0,0);
                textAlign(CENTER);
                textSize(30);
                if (squares[i][j].letter != '.'){
                    text(Character.toUpperCase(squares[i][j].letter),squares[i][j].posX, squares[i][j].posY-700);
                }
            }
        }
    }
    public void keyPressed(){
        switch (currentGameState){
            case RUNNING -> {
                if (Character.isLetter(key) && currentNum <= 4){
                    currentGuess = currentGuess + key;
                    squares[guessNum][currentNum].letter = key;
                    currentNum += 1;
                }
                else {
                    switch (key) {
                        case BACKSPACE, DELETE -> {
                            if (currentGuess.length() != 0) {
                                invalid = false;
                                squares[guessNum][currentNum - 1].letter = '.';
                                currentGuess = currentGuess.substring(0, currentGuess.length() - 1);
                                currentNum -= 1;
                            }
                        }
                        case RETURN,ENTER -> {
                            try {
                                if (currentGuess.length() == 5 && isInFile(currentGuess)){
                                    invalid = false;
                                    checkTiles();
                                    currentNum = 0;
                                    guessNum += 1;
                                    currentGuess = "";
                                    if (guessNum == 6){
                                        endScreen(false);
                                    }
                                }
                                else {
                                    invalid = true;
                                }
                            } catch (IOException e) {

                            }
                        }
                    }
                }
            }
            case FINISHED -> {
                for (int i = 0; i<=5; i++) {
                    for (int j = 0; j <= 4; j++) {
                        squares[i][j].status = "NONE";
                        squares[i][j].letter = '.';
                    }
                }

                gameNum += 1;
                guessNum = 0;
                currentNum = 0;
                answer = readFile(random.nextInt(2135)+1);
                currentGameState = GameState.RUNNING;

            }
        }

    }
    public void mousePressed(){
        switch (currentGameState){
            case FINISHED -> {
                for (int i = 0; i<=5; i++) {
                    for (int j = 0; j <= 4; j++) {
                        squares[i][j].status = "NONE";
                        squares[i][j].letter = '.';
                    }
                }

                gameNum += 1;
                guessNum = 0;
                currentNum = 0;
                answer = readFile(random.nextInt(2135)+1);
                currentGameState = GameState.RUNNING;
            }
            default -> {

            }
        }
    }
    public void checkTiles(){
        if (answer.equals(currentGuess)){
            endScreen(true);
        }
        for (int i = 0; i <=4; i++){
            if (currentGuess.charAt(i) == answer.charAt(i)){
                squares[guessNum][i].status = "GREEN";
            }
            else {
                for (int j = 0; j<5;j++){
                    if (currentGuess.charAt(i) == answer.charAt(j)){
                        squares[guessNum][i].status = "YELLOW";
                    }
                }
                if (squares[guessNum][i].status == "NONE"){
                    squares[guessNum][i].status = "GRAY";
                }
            }
        }
    }
    public void endScreen(boolean won){
        currentGameState = GameState.FINISHED;
        fill(0,0,0);
        rect(45,45,510,660);
        fill(255,255,255);
        rect(50,50,500,650);
        fill(0,0,0);
        textAlign(CENTER);
        textSize(100);
        if (won){
            text("Nice Job!",300,140);
            textSize(70);
            text("Score: " + (guessNum + 1), 300,250);
            avgScore = (float) Math.round(((avgScore * (gameNum - 1) + guessNum + 1) / gameNum) * 100) /100;

            text("Avg Score: " + (avgScore), 300,400);
        }
        else {
            text("You Lost!",300,140);
            textSize(70);
            avgScore = (float) Math.round(((avgScore * (gameNum - 1) + guessNum + 1) / gameNum) * 100) /100;
        }

        text("Avg Score: " + (avgScore), 300,300);
        textSize(50);
        text("The word was " + answer,300,200);
        textSize(20);
        text("Press any key to try again", 300,680);

        guessNum = 0;
    }
    public String readFile(int lineNum) {
        String line;
        try (Stream<String> lines = Files.lines(Paths.get("possibleWords.txt"))) {
            line = lines.skip(lineNum).findFirst().get();
            return line;
        }
        catch(IOException e){
        }
        return null;
    }
}
