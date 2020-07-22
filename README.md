# Project-covid88

<p>Discipline Programming II at Faculdade de Ciências da Universidade de Lisboa taught by Professor António Branco.</p>

<h2>Objective</h2>
<p>In this project, with a pedagogical purpose, using Python 3, the defeatCOVID88 software is implemented, which allows determining the time for the spread of COVID88 disease from one individual to another within a social network. The program delivers the time (in number of hours) that one of these two elements takes to be infected with COVID88 if the other contracts the disease.</p>

<h2>Input</h2>
<p>The program receives a file with pairs of names, and a file containing the description of a social network in which the Direct field of a given line stores the IDs of the elements in direct social contact with the element described in that line, Fitness indicates the level of the health status (1 to 5 maximum), and Immune indicates whether the person described in that row is immune or not.</p>

<h2>Output</h2>
<p>
<ul>
<li>"X out of the social network " if X is not on the network;</li>
<li>or "No contagion between A and B " if there is no propagation of
COVID88 between A and B;</li>
<li>or an integer (obtained by rounding), which indicates the number of hours
it takes the spread of COVID88 between A and B, otherwise.</p></li>
</ul>
</p>

<h2>General specification</h2>
<p>
<ul>
<li>COVID88 disease has the specific characteristic of spreading only between non-immune elements in a direct social relationship and transiently between elements in an intermediary social relationship, all of them not immune.</li>
<li>Between two elements A and B not immune in a direct social relationship, B becomes infected after H days after A contracts the disease, in which H is obtained, in days, by the level of B's ​​health multiplied by the inverse of age from A.</li>
<li>Direct social relations are symmetrical, that is, if B is in the direct relation of A, likewise A is in the direct relation of B (even if only one of these two directions is registered in the network).</li>
</ul>
</p>

<h2>Running</h2>
<p>The software is run using the following command line instruction:</p>

```
$ python defeatCOVID88.py inputFile1.txt inputFile2.txt outputfile.txt
```

<p>wherein:
<ul>
<li>inputFile1.txt it is a file with the social network;</li>
<li>inputFile2.txt it is a file with a pair of names per line;</li>
<li>e outputfile.txt is the name of the file in which the results are written for each pair present in inputFile2.txt, in the respective order of inputFile2.txt;</li>
<ul>
</p>

<h2>Developers</h2>
<p>
<ul>
<li>Julliana dos Santos e Sousa</li>
<li>Sofia Pedro Maciel Lourenço</li>
</ul>
</p>
