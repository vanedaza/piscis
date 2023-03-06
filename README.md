# PISCIS : Platform for Interactive Search and Citizen Science

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/ivco19/libs.svg?branch=master)](https://travis-ci.com/github/vanedaza/piscis)
[![Documentation Status](https://readthedocs.org/projects/piscis/badge/?version=latest)](https://piscis.readthedocs.io/en/latest/)
[![https://github.com/leliel12/diseno_sci_sfw](https://img.shields.io/badge/DiSoftCompCi-FAMAF-ffda00)](https://github.com/leliel12/diseno_sci_sfw)
[![Article](http://astronomiaargentina.fcaglp.unlp.edu.ar/b62/2021BAAA...62..310D.pdf)]



<div class="alert alert-block alert-warning">

<table><tr><td><img src='log_piscis.png'></td></tr></table>
</div>

Piscis is an app that allows users to vote for the type of interaction observed in images of galaxies pair. 

This is app was built used Django framework. Django is a Python-based free and open-source web framework, which follows the model-template-view (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established as a non-profit. 

In particularly the versions used in this project are Django = 2.2, pytz==2019.2 and Python = 3.7. The packages described in **requirements.txt** are necessary to start up.

## Installation

Below we describe how you can install our project without the use of virtual environments and with them.


<div class="alert alert-block alert-warning">
    <b>If you want to install the packages in your usual user, you can use the comand:</b>
           
           
        $ pip install -r /path/to/requirements.txt
</div>



If you prefer, you can create a  virtual environment of conda o pip:

### Conda

<div class="alert alert-block alert-warning">
    <b>create conda enviroment:</b>
           
           
        $ conda create --name environment_name python=3.7

</div>


<div class="alert alert-block alert-warning">
    <b>activate your environment:</b>
           
           
        $ source activate environment_name
</div>

<div class="alert alert-block alert-warning">
    <b>install requirements:</b>
           
           
       $ conda install --force-reinstall -y -q --name piscis -c conda-forge --file requirements.txt
</div>


<div class="alert alert-block alert-warning">
    <b>deactivate your environment:</b>
           
           
       $ conda deactivate
</div>



### Pip

<div class="alert alert-block alert-warning">
    <b>create conda enviroment:</b>
           
           
        $ virtualenv environment_name -p python3

</div>


<div class="alert alert-block alert-warning">
    <b>activate your environment:</b>
           
           
        $ source environment_name/bin/activate
</div>

<div class="alert alert-block alert-warning">
    <b>install requirements:</b>
           
           
       $ pip install -r /path/requirements.txt
</div>


<div class="alert alert-block alert-warning">
    <b>deactivate your environment:</b>
           
           
       $ deactivate
</div>



