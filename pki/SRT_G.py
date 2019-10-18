# -*- coding: utf-8 -*-

"""
@author: Franklin
@file: SRT.py
@time: 2019-10-09 18:09
@dec:
"""
import datetime
import numpy as np

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
        return self.key + self.value


class RadixTree:
    def __init__(self):
        """
        Initialize a Radix Tree
        """
        self.root = RadixNode()

    def insert(self, x, k, val):
        """
        Insert a string at the given node
        :param x: node at which specified string is to be inserted
        :param k: string which is to be inserted at the node
        :return: None
        """
        if k == '':
            x.isLeaf = True
            x.value = val
            return
        combos = getAllStrings(k)
        # print(combos)
        for a in combos:
            # print('a:', a)
            for b in x.children.keys():
                # print("b: ", b)
                if a[0] == b[:len(a[0])]:
                    # print('a[0]: ', a[0], 'b[:'+str(len(a[0]))+']: ', b[:len(a[0])])
                    if a[0] != b:
                        x.children[a[0]] = RadixNode(a[0])
                        x.children[a[0]].children[b[len(a[0]):]] = x.children[b]
                        x.children[a[0]].children[b[len(a[0]):]].key = b[len(a[0]):]
                        if a[1][len(a[0]):] != '':
                            x.children[a[0]].children[a[1][len(a[0]):]] = RadixNode(a[1][len(a[0]):])
                            x.children[a[0]].children[a[1][len(a[0]):]].value = val
                            # RadixNode(a[1][len(a[0]):]).value = val
                            x.children[a[0]].children[a[1][len(a[0]):]].isLeaf = True
                        else:
                            x.children[a[0]].value = val
                            x.children[a[0]].isLeaf = True
                        del x.children[b]
                    else:
                        self.insert(x.children[b], k[len(a[0]):], val)
                    return

        # RadixNode(k).value = val
        x.children[k] = RadixNode(k)

        x.children[k].value = val
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
            # print(a, type(a))
            # print(x.children.keys())
            key = '.'.join(a[0])
            # print(key, x.children.keys())
            if key in x.children.keys():

                return "ID: {id}, Pubkey: {pubkey}".format(id=key, pubkey=x.children[key].value)

                # k = '.'.join(k)
                #
                # return self.search(x.children[key], k[key:])
            # if a[0] in x.children.keys():
            #     return self.search(x.children[a[0]], k[len(a[0]):])

        return False


    def searchPrefix(self, x, k):
        """
        模糊查询
        :param x:
        :param k:
        :return:
        """
        if k == '':
            return x.leafOrNot()


        for a in getAllStrings(k):
            key = '.'.join(a[0])
            for keys in x.children.keys():
                # print("keys: ", keys, " key: ", key)
                if key in keys:
                    return "ID: {id}, Pubkey: {pubkey}".format(id=keys, pubkey=x.children[keys].value)

        return False


    def updatePubkey(self, x, k, val):
        """
        模糊查询
        :param x:
        :param k:
        :return:
        """
        if k == '':
            return x.leafOrNot()

        for a in getAllStrings(k):
            # print(a, type(a))
            # print(x.children.keys())
            key = '.'.join(a[0])
            # print(key, x.children.keys())
            if key in x.children.keys():
                x.children[key].value = val
                return "UPDATE IS OK! ID: {id}, Pubkey: {pubkey}".format(id=key, pubkey=x.children[key].value)


        return False

    def deleteID(self, x, k):
        """
        模糊查询
        :param x:
        :param k:
        :return:
        """
        if k == '':
            return x.leafOrNot()

        for a in getAllStrings(k):
            # print(a, type(a))
            # print(x.children.keys())
            key = '.'.join(a[0])
            # print(type(x.children), x.children)
            if key in x.children.keys():
                x.children.pop(key)

                return True
                # print(type(x.children), x.children)


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
                print("string:{string}, ID:{id}, Pubkey:{pubkey}".format(string=string, id=a, pubkey=x.children[a].value))
                # print(string + a + x.children[a].value)
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

    lis = string.split('.')
    for a in range(len(lis), 0, -1):

        yield (lis[:a], lis)


def main():
    print("Tree 1:")
    R = RadixTree()
    for i in range(0, 10):
        R.insert(R.root, "cn.bj.edu."+str(i)+".bistu.a", "test.a."+str(i))
        # R.insert(R.root, "cn.bj.edu.bistu.a." + str(i) , "a.test." + str(i))

    print(R.updatePubkey(R.root, "cn.bj.edu.8.bistu.a", "test.a.update.Test"))
    R.deleteID(R.root, "cn.bj.edu.8.bistu.a")
    t1 = datetime.datetime.now()
    R.search(R.root,"cn.bj.edu.8.bistu.a")
    R.searchPrefix(R.root, "cn.bj.edu.")
    t2 = datetime.datetime.now()
    print((t2-t1).microseconds)

    # R.print_tree(R.root,'')
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

def getTime(n,num):
    insertT = 0
    updateT = 0
    searchT = 0
    searchPT = 0
    deleteT = 0

    R = RadixTree()
    for i in range(0,n):
        R.insert(R.root, "cn.bj."+ str(i) + "edu" , "test." + str(i))
        # print(m)
    for i in range(0, num):
        a = np.random.randint(0, n, 1)
        b = np.random.randint(n,2*n,1)

        insertT1 = datetime.datetime.now()
        R.insert(R.root,"cn.bj."+ str(b) + "edu" , "test." + str(b))
        insertT2 = datetime.datetime.now()
        insertT += (insertT2-insertT1).microseconds

        updateT1 = datetime.datetime.now()
        R.updatePubkey(R.root, "cn.bj." + str(a) + "edu", "test.a.update.Test")
        updateT2 = datetime.datetime.now()
        updateT += (updateT2-updateT1).microseconds

        searchT1 =  datetime.datetime.now()
        R.search(R.root, "cn.bj." + str(a) + "edu")
        searchT2 =  datetime.datetime.now()
        searchT += (searchT2 - searchT1).microseconds

        searchPT1 =  datetime.datetime.now()
        R.searchPrefix(R.root, "cn.bj")
        searchPT2 =  datetime.datetime.now()
        searchPT += (searchPT2 - searchPT1).microseconds

        deleteT1 =  datetime.datetime.now()
        R.deleteID(R.root, "cn.bj."+str(a)+"edu")
        deleteT2 =  datetime.datetime.now()
        deleteT = (deleteT2 - deleteT1).microseconds




    print("Time on insert:{num}次：已有节点：{n},节点总时间：{time}微秒， 平均时间：{time1}微秒。".format(num=num, n=n, time=insertT, time1=insertT / num))
    print("Time on update:{num}次：已有节点：{n},总时间：{time}微秒， 平均时间：{time1}微秒。".format(num=num,n=n, time=updateT, time1=updateT / num))
    print("Time on search:{num}次：已有节点：{n},总时间：{time}微秒， 平均时间：{time1}微秒。".format(num=num,n=n, time=searchT, time1=searchT / num))
    print("Time on searchPrefix:{num}次：已有节点：{n},总时间：{time}微秒， 平均时间：{time1}微秒。".format(num=num, n=n,time=searchPT, time1=searchPT/ num))
    print("Time on delete:{num}次：已有节点：{n},总时间：{time}微秒， 平均时间：{time1}微秒。".format(num=num, n=n, time=deleteT, time1=deleteT / num))

if __name__ == '__main__':
    # main()
    for i in range(7,9):
        getTime( i * 10000, 100)