# -*- coding: utf-8 -*-

"""
@author: Franklin
@file: SRT.py
@time: 2019-10-09 18:09
@dec: 
"""

class RadixNode:
    def __init__(self, k=None, val=None):
        """
        Initialize a Radix Tree Node
        :param k: key value of the node (default None)
        """
        self.key = k
        self.children = {}
        self.value = val
        self.isLeaf = False

    def leafOrNot(self):
        """
        Check if the node is a leaf or not
        :return: Boolean
        """
        return self.isLeaf

    def __str__(self):
        """
        Specify the string to be returned when the Node is printed
        :return: String
        """
        return self.key


class RadixTree:
    def __init__(self):
        """
        Initialize a Radix Tree
        """
        self.root = RadixNode()

    def insert(self, x, k):
        """
        Insert a string at the given node
        :param x: node at which specified string is to be inserted
        :param k: string which is to be inserted at the node
        :return: None
        """
        if k == '':
            x.isLeaf = True
            return
        combos = getAllStrings(k)
        # print(combos)
        for a in combos:
            # print('a:', a)
            for b in x.children.keys():
                # print("b: ", b)
                if a[0] == b[:len(a[0])]:
                    print('a[0]: ', a[0], 'b[:len(a[0])]: ', b[:len(a[0])])
                    if a[0] != b:
                        x.children[a[0]] = RadixNode(a[0])
                        x.children[a[0]].children[b[len(a[0]):]] = x.children[b]
                        x.children[a[0]].children[b[len(a[0]):]].key = b[len(a[0]):]
                        if a[1][len(a[0]):] != '':
                            x.children[a[0]].children[a[1][len(a[0]):]] = RadixNode(a[1][len(a[0]):])
                            x.children[a[0]].children[a[1][len(a[0]):]].isLeaf = True
                        else:
                            x.children[a[0]].isLeaf = True
                        del x.children[b]
                    else:
                        self.insert(x.children[b], k[len(a[0]):])
                    return
        x.children[k] = RadixNode(k)
        x.children[k].isLeaf = True

    def search(self, x, k):
        """
        Search for a string at the given node
        :param x: node at which specified string is to be searched for
        :param k: string which is to be searched for at the node
        :return: None
        """
        if k == '':
            return x.leafOrNot()
        for a in getAllStrings(k):
            if a[0] in x.children.keys():
                return self.search(x.children[a[0]], k[len(a[0]):])
        return False

    def print_tree(self, x, string):
        """
        Print the complete sorted tree
        :param x: node at which leaves are searched for
        :param string: contains the string that is formed by parent nodes of x
        :return: None
        """
        for a in sorted(x.children.keys()):
            if x.children[a].isLeaf:
                print(string + a)
            self.print_tree(x.children[a], string + a)

    def spell_checker(self, string):
        """
        Checks is a string exists in the tree
        :param string: string whose validity is to be checked
        :return: Boolean
        """
        return self.search(self.root, string)


def getAllStrings(string):
    """
    Yield all string instances from index 0, decreasing string length by 1 at each iteration
    :param string: the string whose instances are to be found
    :return: Tuple
    """


    for a in range(len(string), 0, -1):

        yield (string[:a], string)


def main():
    print("Tree 1:")
    R = RadixTree()
    R.insert(R.root, "hello")
    R.insert(R.root, "hello1")

    R.print_tree(R.root,'')
    # f = open('word_list/words_44k.txt')
    # words = f.readlines()
    # words = [line[:-1] for line in words]
    # for a in words:
    #     R.insert(R.root, a)
    # word = input("Enter a word to check its validity: ")
    # if R.spell_checker(word):
    #     print("Correct spelling")
    # else:
    #     print("Incorrect spelling")
    # print("Tree 2:")
    # R2 = RadixTree()
    # words = ["hey", "hi", "hello", "tailoring", "tailor", "tailoring"]
    # for word in words:
    #     R2.insert(R2.root, word)
    # R2.print_tree(R2.root, "")


if __name__ == '__main__':
    main()