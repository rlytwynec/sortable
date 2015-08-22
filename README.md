# Sortable Programming Challenge Submission

## What is it?

The full description for the programming challenge can be found [here](http://sortable.com/challenge/).

To summarize: the objective is to match products from a single catalog with listings on an eCommerce site. Both datasets are formatted in a different manner and the listings are from a variety of different vendors with variations in formatting. Emphasis is placed on minimizing the number of false positives over maximizing the number of matches.

This project was completed using Python 2.7 in Windows 7 using IDLE.

## Neat! What's in this repo?

Everything has been sorted into four folders:

###Compiled

This contains the compiled code including the products.txt and listings.txt data files required to run the program, all wrapped up in a nice little package for you.

To run, download the entire folder and run either "match" or "match_verbose". "match_verbose" provides numerical analysis of the data including the number of matches made.

###Data Files

This contains the sample data files provided by Sortable (listings and products) as well as a results file. This file contains the results of running my code given the provided sample data.

###Documentation

Background describes the problem as well as my approach and some preliminary analysis of the data. Analysis contains the results as well as a comparison to other matching techniques.

###Source Code

Pretty self explanatory. This contains the .py files for all of the code used for this project.

##Cool, so how do I run it?

If you've got Python 2.7 installed, it's as easy as downloading the repo, navigating to the Compiled folder and running either "match.pyc" or "match_verbose.pyc". To use different data files, simply replace the products and listings files with different files of the same name.

This has been tested in Win7 and Win10. To get this running on Linux, the line break format may need to be converted.
