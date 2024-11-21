#include <iostream>
#include <string>
using namespace std;

class Human {
    public:
        string GetProfession() {
            return profession;
        }
    protected:
        Human() {}  
        string profession;
    private:
        virtual void SetProfession() = 0;
};

class Student: public Human {
    private:
        void SetProfession() override {
            profession = "Student";
        }
    public:
        Student(): Human() {
            SetProfession(); 
        }
};

class Teacher: public Human {
    private:
        void SetProfession() override {
            profession = "Teacher";
        }
    public:
        Teacher(): Human() {
            SetProfession();
        }
};

class PairGame {
    protected:
        Human* playerOne;
        Human* playerTwo;
    public:
        PairGame(): playerOne(nullptr), playerTwo(nullptr) {}
        
        void SetPlayerOne(Human* player) {
            playerOne = player;
        }
        void SetPlayerTwo(Human* player) {
            playerTwo = player;
        }
        virtual void Play() = 0;
};

class Chess: public PairGame {
    public:
        void Play() override {
            cout << "Playing Chess with " << playerOne->GetProfession() << " and " << playerTwo->GetProfession() << endl;  
        }
};

class Checkers: public PairGame {
    public:
        void Play() override {
            cout << "Playing Checkers with " << playerOne->GetProfession() << " and " << playerTwo->GetProfession() << endl;
        }
};

int main() {
    Student student;
    Teacher teacher;
    Chess chessGame;
    Checkers checkersGame;

    chessGame.SetPlayerOne(&student);
    chessGame.SetPlayerTwo(&teacher);
    chessGame.Play();

    checkersGame.SetPlayerOne(&student);
    checkersGame.SetPlayerTwo(&teacher);
    checkersGame.Play();

    return 0;
}
