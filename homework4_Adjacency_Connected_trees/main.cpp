#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

// Структура для представления узла дерева
struct TreeNode {
    int data;
    vector<TreeNode*> children;

    TreeNode(int val) : data(val) {}
};

// Класс для представления дерева
class Tree {
private:
    TreeNode* root;

public:
    Tree(int rootVal) {
        root = new TreeNode(rootVal);
    }

    // Функция для добавления ребра между двумя узлами дерева
    void addEdge(int parentVal, int childVal) {
        TreeNode* parentNode = findNode(root, parentVal);
        if (parentNode != nullptr) {
            TreeNode* childNode = new TreeNode(childVal);
            parentNode->children.push_back(childNode);
        } else {
            cout << "Родительский узел не найден." << endl;
        }
    }

    // Функция для поиска узла с определенным значением в дереве
    TreeNode* findNode(TreeNode* node, int val) {
        if (node == nullptr) return nullptr;
        if (node->data == val) return node;

        for (TreeNode* child : node->children) {
            TreeNode* found = findNode(child, val);
            if (found != nullptr) return found;
        }

        return nullptr;
    }

    // Функция для вывода дерева в смежном представлении
    void printAdjacency() {
        cout << "Смежное представление дерева:" << endl;
        printAdjacencyUtil(root);
    }

    // Функция для вывода дерева в связном представлении
    void printConnected() {
        cout << "Связное представление дерева:" << endl;
        unordered_set<int> visited;
        printConnectedUtil(root, visited);
    }

    // Вспомогательная функция для вывода смежного представления дерева (рекурсивная)
    void printAdjacencyUtil(TreeNode* node) {
        if (node == nullptr) return;

        cout << node->data << ": ";
        for (TreeNode* child : node->children) {
            cout << child->data << " ";
        }
        cout << endl;

        for (TreeNode* child : node->children) {
            printAdjacencyUtil(child);
        }
    }

     void printConnectedUtil(TreeNode* node, unordered_set<int>& visited) {
        if (node == nullptr) return;

        visited.insert(node->data);

        cout << node->data << ": ";
        for (TreeNode* child : node->children) {
            cout << child->data << " ";
            if (visited.find(child->data) == visited.end()) {
                printConnectedUtil(child, visited);
            }
        }
        cout << endl;
    }
};

int main() {
    // Создание дерева
    Tree tree(1);
    tree.addEdge(1, 2);
    tree.addEdge(1, 3);
    tree.addEdge(2, 4);
    tree.addEdge(2, 5);
    tree.addEdge(3, 6);

    // Вывод дерева в смежном представлении
    tree.printAdjacency();

    // Вывод дерева в связном представлении
    tree.printConnected();

    return 0;
}