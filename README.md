Description
===========
This package is to infer evolutionary tree of tumor cells thourgh integer copy number profile from single cell sequencing technology. It will estimate:
* An rooted directed minimal spanning tree to represent evolution of tumor cells
* The segmental (gene) copy number events associated with specific lineage


System requirements and dependency
==================================
This package runs on Python 2.7.

It also requires R 3.5
to run and has dependency on the R packages:

	igraph, HelloRanger and DescTools.



Installation
============
Please download and copy the distribution to your specific location. If you are cloning from github, ensure that you have git-lfs installed.

For example, if the downloaded distribuition is RDMST.tar.gz.
	Type 'tar zxvf RDMST.tar.gz'

Then, run scTree.py in the resulting folder.

Usage
=====
```
Options:
  --version             show program's version number and exit
  -h, --help            Show this help message and exit.
  -P PATH, --PATH=PATH
                        the path of RDMST package
  -I INPUT, --Input=INPUT
                        the input file is integer copy number profile estimated from scDNA-seq or scRNA-seq
  -O OUTPATH, --outpath=OUTPATH
                        the output path.
  -D DATATYPE, --DATATYPE=DATATYPE     the input file type either D (scDNA-seq) or R (scRNA-seq)
  -W WINDOWS, --WINDOWS=WINDOWS
                        The size of smoothing windows if your inputfile is from scRNA-seq.
                        The value is the number of genes which will be merge. Default value is 30.


```

Input files
===========

DNA input files:

	Two kinds of input files are allowed in RDMST:

	(1) Integer copy number profile from scDNA-seq

	(2) Infered copy number profile from scRNA-seq;


  *scDNA-seq input*

  	chr	pos	cell1  cell2 cell3 ......
  	chr1	977836	2  3 1 ......
  	chr1	1200863	3 3 1	......

  *scRNA-seq input*

    	cell1  cell2 cell3 ......
    gene1	2  3 1 ......
    gene2	3 3 1	......


Run RDMST package
============

    Python scTree.py [-O <output path>] [-W <smoothing window size>] –P <RDMST package path> –I <input file> -D <input file type>
    [...] contains optional parameters. The mandatory arguments are -P, -I and -D. The input file type is either "D" or "R".
By default, -W is 30, which defines the smoothing window as 30 adjacent gene.


Examples
========
Try RDMST in the package directory on the different example datasets

**Example 1: Input from scDNA-seq data**

	python scTree.py -P ./ -I ./example/scDNA.CNV.txt -D D -O ./example/output

**Example 2: Input from scRNA-seq data**

	python scTree.py -P ./ -I ./example/scRNA.inferCNV.txt -D R -O ./example/output1 -W 30


Output files
============

Three text files:

	(1) CNV.tree.txt file: an rooted directed tree and the visualization of the tree

	(2) segmental.LSA.txt file: significant lineage-specific CNAs at segment level

	(3) gene.LSA.txt file: significant lineage-secific CNAs at gene level. RDMST includes
                          more than 400 cancer associated genes which are from 11 oncigenic pathways:
                          DDR, Notch, PI3K, Hippo, RTK/RAS, MYC, p53, Nrf2, TGFB, Wnt and cellcycle.

Two figures:

	(1) singlecell.tree.pdf: the RDMST of cells visualized by igraph

	(2) LSA.tree.pdf: the RDMST of lineage-specific CNAs visualized by igraph


Developer
=========
Fang Wang (fwang9@mdanderson.org), Qihan Wang (Chuck.Wang@rice.du)

Draft date
==========
Oct. 30, 2019
