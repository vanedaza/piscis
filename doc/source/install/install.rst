Installation
============

Below we describe how you can install our project without the use of virtual environments and with them.



If you want to install the packages in your usual user, you can use the comand:
           
    .. code-block:: console

        $ pip install -r /path/to/requirements.txt




If you prefer, you can create a  virtual environment of conda o pip:

Conda
-----

Create conda enviroment

   .. code-block:: console           
           
        $ conda create --name environment_name python=3.7




Activate your environment:

    .. code-block:: console              
           
        $ source activate environment_name

Install requirements:

    .. code-block:: console            
           
       $ conda install -r /path/requirements.txt



Deactivate your environment:

    .. code-block:: console             
           
       $ conda deactivate



Pip
---


Create conda enviroment:

    .. code-block:: console           
           
        $ virtualenv environment_name -p python3



Activate your environment:
           
    .. code-block:: console   

        $ source environment_name/bin/activate

Install requirements:
           
    .. code-block:: console 

       $ pip install -r /path/requirements.txt



Deactivate your environment:

    .. code-block:: console            
           
       $ deactivate
