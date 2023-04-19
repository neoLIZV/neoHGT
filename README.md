
<p align="center">
	<a href="https://github.com/neoLIZV/neoHGT">
		<img src="./neoHGT.png" width="250">
	</a><br>
</p>

# neoHGT2: Horizontal Gene Transfer

Updated on April 2023.

To see the previous version neoHGT1, you may visit [here](https://www.github.com/cgneo/neoHGT)


## Table of Contents
1. [About](#about)
2. [Installation](#installation)
3. [Database](#database)
4. [Search](#search)
5. [Analyze](#analyze)
6. [Lastly](#lastly)
7. [License](#license)
8. [Copyright](#copyright)

## About
**neoHGT** can predict the horizontal/lateral gene transfer (HGT) for species of interest. This project is based on [HGTector](https://github.com/qiyunlab/HGTector) developed by Qiyun lab, but the difference is that I have fixed some known bugs, optimized the downloading process by leveraging multi-processing, and improving the overall stability of the software.

  


## Installation
The project is written in Python3.<br>
Recommended installation method:

Step 1/3:

```
conda create -n neoHGT -c conda-forge python=3 pyyaml pandas matplotlib scikit-learn
```

Step 2/3:

Next, you will need to manually install diamond by visiting [the official conda webpage](https://anaconda.org/bioconda/diamond/files).

You will see a list of files, please look at the begining of the filename, which describes the operating system. After downloading the one that corresponds to your system, you can run

```
conda install
```

followed by the file you just downloaded (dragging the file to your teminal) to install diamond.

Step 3/3:

Run the following command:

```
conda activate neoHGT
pip install git+https://github.com/neoLIZV/neoHGT.git
```


## Database

![Database comparison between HGTector and neoHGT](./Database.gif)

Compared to HGTector, neoHGT not only fixes some known bugs of HGTector but also uses multi-processes to enable parallel downloading, saving you time on the database downloading process.

The command that I used to build the database is:

```
neoHGT database -c bacteria,archaea -o <FOLDER_NAME>
```

where ```-c``` or equivalently ```-cats``` means category.

This following table explains the command and options available for you to build a customized database.

| Command | Options |
|---------|---------|
| -c (-cats)      | archaea, bacteria, fungi, invertebrate, plant, protozoa, vertebrate_mammalian, vertebrate_other, and viral |
| -o      | Output database directory |

For more advanced options such as excluding specific taxids, please refer to HGTector's [Database](https://github.com/qiyunlab/HGTector/blob/master/doc/database.md) documentation.

Known issue:

Don't panic if you see this error message:
```
File "/Users/___/miniconda3/envs/neoHGT/lib/python3.11/site-packages/neoHGT/database.py", line 351, in get_categories
    raise ValueError(
ValueError: "___" is not a valid RefSeq genome category
```

This error occurs when the NCBI server has temporarily shuted-down the connection from you (refused your connection). There is nothing wrong with the program itself.

The best thing you can do when having this error is to test your connection by entering the following command to the terminal:

```
rsync --list-only --no-motd rsync://ftp.ncbi.nlm.nih.gov/genomes/refseq/
```

If you see something like ```rsync: failed to connect to ftp.ncbi.nlm.nih.gov: Connection refused (61)
rsync error: error in socket IO (code 10)```, it confirms that, indeed, there is a network issue (likely from the NCBI server side).

Otherwise, if the previous command returns you a list that starts with ```drwxr-sr-x```, followed by something like ```lrwxrwxrwx```, it means the connection is restored, and you can safely execute the program again.

## Search

neoHGT added `try` and `except` to make the searching process more robust.

To perform a search, please refer to [HGTector's Search](https://github.com/qiyunlab/HGTector/blob/master/doc/search.md) documentation.

## Analyze

neoHGT changed the output format of the graph from `.png` to `.pdf` for better resolution and publication purposes.

To perform analysis, please refer to [HGTector's Analyze](https://github.com/qiyunlab/HGTector/blob/master/doc/analyze.md) documentation.


## Lastly

To uninstall, you may run:
```
conda remove -n neoHGT --all
conda uninstall bioconda
```

For comprehensive guideline, please refer to [HGTector's Installation](https://github.com/qiyunlab/HGTector/blob/master/doc/install.md) for full information.


## Publication

This repository was a result of my internship at LOB - Laboratoire d'Optique et Biosciences, where we published a paper on [Nature Communication](https://www.nature.com/articles/s41467-023-36487-z).

> Filée, J., Becker, H. F., Mellottee, L., Eddine, R. Z., Li, Z., Yin, W., Lambry, J.-C., Liebl, U., & Myllykallio, H. (2023, February 15). Bacterial origins of thymidylate metabolism in Asgard Archaea and Eukarya. Nature Communication. Retrieved February 18, 2023, from https://www.nature.com/articles/s41467-023-36487-z



## Works cited

> Zhu Q, Kosoy M, Dittmar K. HGTector: [an automated method facilitating genome-wide discovery of putative horizontal gene transfers](https://bmcgenomics.biomedcentral.com/articles/10.1186/1471-2164-15-717). *BMC Genomics*. 2014. 15:717.


## License

Copyright (c) 2023-, [neoLIZV](https://github.com/neoLIZV). Licensed under [BSD 3-clause](http://opensource.org/licenses/BSD-3-Clause).

Copyright (c) 2013-, [Qiyun Zhu](mailto:qiyunzhu@gmail.com) and [Katharina Dittmar](mailto:katharinad@gmail.com). Licensed under [BSD 3-clause](http://opensource.org/licenses/BSD-3-Clause). See full license [statement](LICENSE).
