# MDA-Project-Tree-Inference

This package is to generate evolutionary trees. Please insert your parameters in "param.txt" 
and then run "final_package.py" to generate tree.

Output tree of this algorithm is expressed in maps. It takes the structure that every node is matched to a map, 
this map have key that specifies what the end node is for each edge, and have value that gives the weight on this edge.

For example: <br/>
{A:{B:2}, B{}, C{A:1}} represents <br/>
A -> B == 2 <br/>
C -> A == 1 <br/>