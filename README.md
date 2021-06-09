# Preparatory Assignment

The purpose of this preparatory assignment is to make sure that you (and your computer) are well prepared for the block course to avoid having technical issues inbetween. Therefore, this __assignment is mandatory__ and has to be __submitted until Tuesday, July 27th__ through GitHub. (You will learn how to do this in this assignment)

After you have completed this assignment you will be able to ...

*  name different best practice methods for scientific computing
*  install and configure all required software for the course
*  use Jupyter notebook to write Python code
*  use git and GitHub to track your work progress. 

#### Important notes: 

* Please make sure to __name the output files exactly as described.__
* If you encounter problems which you cannot solve on your own, **post your question in the MS Teams "Preparatory Assignment" channel.** 


## 0. Create a GitHub Account

For this assignment and the block course you will need a [free GitHub user account](https://github.com/). Create a new account if you don't have one already and **send your GitHub user name** to [christina.ludwig@uni-heidelberg.de](mailto:christina.ludwig@uni-heidelberg.de) 

**Note:** For privacy reasons, you do **not** have to use your university email address or provide any personal information in your GitHub account.  


## 1. Fork and clone the preparatory assignment 

1. Go to [https://github.com/advanced-geoscripting-2021/preparatory-assignment](https://github.com/advanced-geoscripting-2021/preparatory-assignment), which includes all material for the assignment. Fork this repository by clicking on the "Fork" button on the upper right corner. Now you have a copy of the original repository in your github account. Make sure to **only use your forked repository** from now on. 

2. Clone your **forked repository** to your computer. Open the command line (git bash on windows) and move to a directory where you want to store the repository. Afterwards, execute the following command to clone the repository. Make sure to **replace "your-github-user-name" with your github user name** to clone your forked repo and not the original one.

```
$ git clone https://github.com/your-github-user-name/preparatory-assignment.git
```

--> Watch [this tutorial video](https://www.youtube.com/embed/yfFbOUnbE1Y) from last year if you need help. Note that some things might be different (e.g. the file names, repository name), but the principle is the same. 


## 2. Best Practices in Scientific Computing

<img src="./img/phdcomic_final.png" alt="final" width="300px" align="right" />

Read the paper by [Wilson et al. (2014)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3886731/) on Best Practices for Scientific Computing and answer the following questions. Write your answer in a Markdown file called _scientific\_programming.md_. Read this [Guide on markdown](https://guides.github.com/features/mastering-markdown/) to format your file. 

1. The paper describes several problems scientist face when performing scientific data analyses. From your experience in performing GIS and general data analyses, which of these problems seem familiar to you? Have you faced other problems not mentioned in the paper? (~100 words)
2. Which methods described in the paper could help you avoid these problems in the future? (~100 words)
3. One of the recommendations by [Wilson et al. (2014)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3886731/) for scientists is to use a Version Control System (VCS). Briefly explain in your own words, what the benefits of VCS are in the context of scientific analyses. (~100 words)

<sup>Image source: “Piled Higher and Deeper” by Jorge Cham, http://www.phdcomics.com</sup>

## 3. Install required software

1. Follow the instructions given in the file [Software Setup](./software_setup.md) to install and configure all software that is required for the course on your computer. 

2. Afterwards, execute [_check\_environment.py_](./check_environment.py) from within your new Python environment to verify that all required packages have been installed successfully. Using the following command the output of the program will be written to a new text file called _check\_environment\_result.txt_. Make sure that you don't get any import errors. 

	```
	$ python check_environment.py > check_environment_result.txt
	```

3. Check whether the new environment is also available within PyCharm by executing the file [_check\_environment.py_](./check_environment.py) from within the [Python Console in PyCharm](https://www.jetbrains.com/help/pycharm/interactive-console.html).

## 4. Using git and Jupyter Notebooks

In this last section, you will use git to track the changes of the files that we have created so far. If you are not familiar with git yet, work through the section [Introduction to git](./git_introduction.md) before continuing with the exercises. 
	
### 4.1 Track your changes using git

In exercises 1 and 2 you have created two files. Copy these files into the main folder of the cloned repository. Create a commit for each one of them in order to track them in your local git repository, e.g.

```
$ git add scientific_programming.md
$ git commit -m "added scientific_programming.md" 
```

--> Watch [this tutorial video](https://www.youtube.com/embed/kVCLIPHfPDo) from last year if you need help. Note that some things (e.g. the file names, repository name) might be different, but the principle is the same. 


### 4.2 Create a new Jupyter notebook

1. Activate the _advgeo_ environment and start a Jupyter Notebook server. 

	``` 
	$ conda activate advgeo
	$ jupyter notebook
	```
	
2. Create a new Jupyter notebook using the Python 3 kernel and name it _preparatory\_assignment.ipynb_.

3. Import the function ```check_packages()``` from _check\_environment.py_ and execute it in order to check whether the notebook is using the right anaconda environment _advgeo_. If you get a ```ModuleImportError```, check whether the right kernel is selected (Jupyter Menu: Kernel &rarr; Change kernel).
4. If everything works, save your notebook and add it to your git repository by creating a new commit.
5. Within the notebook, write a new function called ```list_sum()```, which calculates the sum of all numbers in a list. e.g. 

	``` python
	>>> numbers = [1,2,3,4]
	>>> numbers_sum = list_sum(numbers)
	>>> print(numbers_sum)
	10
	```

6. Create a new commit containing the changes of the notebook. 

### 4.3 Push your commits to GitHub

The last task of this assignment is to push all your commits to GitHub by executing

```
$ git push origin master 
```

Afterwards go to your repository on GitHub and check whether your changes are visible there. 

--> Watch [this tutorial video](https://www.youtube.com/embed/kVCLIPHfPDo) from last year if you need help. Note that some things (e.g. the file names, repository name), but the principle is the same. 

__One last note:__ If you make further edits to your files (e.g. editing your answers to the questions in exercise 3) remember that you can always create new commits containing these changes and push them to your GitHub repository.


### Well done, your ready for the course! :) 







