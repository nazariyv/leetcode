#include <iostream>
#define N 26
using namespace std;

struct TrieNode {
    TrieNode* children[N];
    // you might need some extra values according to different cases
};

/** Usage:
 *  Initialization: TrieNode root = new TrieNode();
 *  Return a specific child node with char c: (root->children)[c - 'a']
 */

int main() {
    TrieNode* root = new TrieNode();
    char c = 'b';
    cout << (root->children)[c - 'a'] << endl;
}
