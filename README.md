# PISCIS : Platform for Interactive Search and Citizen Science

Piscis is an app that allows users to vote for the type of interaction observed in images of galaxies pair. 

This is app was built used Django framework. Django is a Python-based free and open-source web framework, which follows the model-template-view (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established as a non-profit. 

In particularly the versions used in this project are Django = 2.2, pytz==2019.2 and Python = 3.7. The packages described in **requirements.txt** are necessary to start up.

Installation



<div class="alert alert-block alert-warning">
    <b>If you want to install the packages in your usual user, you can use the comand:</b>
           
           
         pip install -r /path/to/requirements.txt
</div>

- pip install -r /path/to/requirements.txt

If you prefer, you can create a virtual environment with some of the commands:

Option 1, for conda:

$conda create --name environment_name python=3.7

activate your environment:
$ source activate environment_name

install requirements:
$ conda install -r /path/requirements.txt

deactivate your environment:
$ deactivate

............................................

Option 2, for pip:

$ virtualenv environment_name -p python3

activate your environment:
$ source environment_name/bin/activate

install requirements:
$ pip install -r /path/requirements.txt

deactivate your environment:
$ deactivate
