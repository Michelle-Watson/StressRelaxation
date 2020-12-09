# Stress Relaxation Test
Data was collected through a lab for the course: BME 281L Mechanics of Deformable Solids Lab.
I usually use excel to process lab data, but wanted to try using Python to practice using the matplotlib, panda, and numPy libraries.
I've added detailed comments throughtout to take you through my thought process, hopefully inspiring you to try switching from excel too!

## Purpose
The purpose of this lab was to examine visoelastic materials and how they differ from elastic materials under constant strain.
Goal: process the data to determine whether the material is viscoelastic or not.
Still a work in progress.

## To run locally
I reccomend downloading Anaconda and creating a virtual environment before running the tool.
* [Install Anaconda](https://docs.anaconda.com/anaconda/install/windows/)
* [Set up environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

<br>  `conda create -n <envName> python`
<br>  `conda activate <envName>`
<br>  `python -m pip install`
<br>  `pip3 install -r requirements.txt` (or just install the libraries listed in Python libraries)

### Python libraries
You can use `conda` or `pip` to install the following:
<br> `conda install pandas`
<br> `conda install numpy`
<br> `conda install matplotlib`

