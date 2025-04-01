#!/bin/bash
echo ""
echo ""
clear
echo "*** LinkedList tests ***"
echo ""

python3 test_LinkedList___str__.py
python3 test_LinkedList_copy.py
python3 test_LinkedList_length.py
python3 test_PersonList.py
python3 test_LinkedList_remove_last.py
python3 test_LinkedList_remove.py
python3 test_LinkedList_to_list.py

echo "--------------------------------"
echo ""
echo ""
echo "****************************************************************"
echo "*** BST tests ***"
echo ""
python3 test_BST__str__.py
python3 test_BST_height.py
python3 test_BST_remove.py
python3 test_BST_to_LinkedList.py
python3 test_BST_to_list.py

echo "Done"