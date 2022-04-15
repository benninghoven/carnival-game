#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

class Contestant {
    private:
        int score;
        string name;
    public:
        Contestant() {
            score = 0;
            name = "PLAYER";
        }
        Contestant(int newScore, string newName) {
            score = newScore;
            name = newName;
        }
        int get_score() const { return score; }
        string get_name() const { return name; }
        void set_score(int newScore) { score = newScore; }
        void set_name(string newName) { name = newName; }

        bool operator>(const Contestant &c) {
            return score > c.score;
        }
        bool operator==(const Contestant &c) {
            if (score == c.score) return name > c.name;
        }
        friend ostream& operator<<(ostream& outs, const Contestant &c) {
            outs << c.name << " " << c.score << endl;
            return outs;
        }
        friend istream& operator>>(istream& ins, Contestant &c) {
            ins >> c.name >> c.score;
            return ins;
        }
};

bool sort_by_score(const Contestant &c1, const Contestant &c2) {
    return c1.get_score() > c2.get_score();
}

int main(int argc, char** argv) {
   cout << "===============   LEADERBOARD   ===============" << endl;
   string filename = "stats.txt";
   fstream file(filename);
   vector<Contestant> contestants;
   if (!file) throw runtime_error("The file name does not exist. Check your directory to see if it is included, or move it if it isn't.\n");
   while (file) {
       string s;
       getline(file, s);
       stringstream read(s);
       string name;
       read >> name;
       if (!file) break;
       int score = 0;
       read >> score;
       if (!file) break;

       Contestant c(score, name);
       contestants.push_back(c);
    }
    sort(contestants.begin(), contestants.end(), sort_by_score);
    for (const Contestant &c : contestants)  cout << setw(23) << c;
}
