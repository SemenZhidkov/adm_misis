// Жидков С.А., Левченко Б.И., Ковалева Мария, Зебелян Артем 

#include <iostream>
#include <vector>
#include <unordered_set>

// Структура для представления узла дерева
struct TreeNode {
    int data;
    std::vector<TreeNode*> children;

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
            std::cout << "Родительский узел не найден." << std::endl;
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
        std::cout << "Смежное представление дерева:" << std::endl;
        printAdjacencyUtil(root);
    }

    // Функция для вывода дерева в связном представлении
    void printConnected() {
        std::cout << "Связное представление дерева:" << std::endl;
        std::unordered_set<int> visited;
        printConnectedUtil(root, visited);
    }

    // Функция для вывода смежного представления дерева (рекурсивная)
    void printAdjacencyUtil(TreeNode* node) {
        if (node == nullptr) return;

        std::cout << node->data << ": ";
        for (TreeNode* child : node->children) {
            std::cout << child->data << " ";
        }
        std::cout << std::endl;

        for (TreeNode* child : node->children) {
            printAdjacencyUtil(child);
        }
    }

    // Функция для вывода связного представления дерева
     void printConnectedUtil(TreeNode* node, std::unordered_set<int>& visited) {
        if (node == nullptr) return;

        visited.insert(node->data);

        std::cout << node->data << ": ";
        for (TreeNode* child : node->children) {
            std::cout << child->data << " ";
            if (visited.find(child->data) == visited.end()) {
                printConnectedUtil(child, visited);
            }
        }
        std::cout << std::endl;
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