# r53_ptr_vpc_associator

This is a program to association reverse zones to vpcs.  It is associated with https://github.com/aws-samples/aws-lambda-ddns-function

Prerequisites
=============

It is highly recommended you run this package within a python virtual environment, so
you do not affect your desktop/laptop.  To setup a python virtual environment, you should make 
sure you have python3 installed, and do the following.

NOTE:  Why am I doing this.  With a python virtual environment, you can create as
many virtual environmentsa as you would like, and with different python versions.  These
virtual environments are isolated in a directory, and will not affect anything else on
your computer.  This way, you can test and ensure things will work.

First, figure out the path to the python version installed on your machine.

    which python3
    /usr/local/bin/python3
    
Next, you should pip install the virtualenv package

    pip install virtualenv
    
Next, you should create a directory, where you are going to keep the virtual environments,
and create a new virtualenv by using the path to the python version you found above.

    mkdir ~/virtual_environments
    cd virtual_environments
    virtualenv -p /usr/local/bin/python3 my_python3_virtualenv
    
To activate the virtual environment

    source ~/virtual_environments/my_python3_virutalenv/bin/activate
    
NOTE:  To deactivate the virtual environment

    deactivate

Installation
============

For general usage:

    pip install r53_ptr_vpc_associator

For local development:

    git clone https://github.com/rubelw/r53_ptr_vpc_associator
    cd r53_ptr_vpc_associator
    pip install --editable .  # Install the local dir as a package, including the 'dev' extras

Example
=======

Getting help

    $ associator --help
    Usage: associator [OPTIONS] COMMAND [ARGS]...
    
    Options:
      --version  Show the version and exit.
      --help     Show this message and exit.
    
    Commands:
      associate  Associated hosted zones to vpc
      zone-list  List vpcs for hosted zones

Listing current zone/vpc associations

    $ associator zone-list --profile-name default
    {
            '/hostedzone/Z1H1CDD4PZKKPB': [
            {
                'VPCRegion': 'us-east-1',
                'VPCId': 'vpc-99999999'
            },
            {
                'VPCRegion': 'us-east-2',
                'VPCId': 'vpc-99999999'
            }
        ]
	}

Associating zones

    $ associator associate --profile-name default --vpc-id vpc-99999999  --vpc-region us-east-2
    [
        'Successfully associated zone: /hostedzone/A3G1CDD4PZKKPB with vpc: vpc-99999999',
        'Successfully associated zone: /hostedzone/HR2F2BVHDW5UD with vpc: vpc-99999999',
        'Successfully associated zone: /hostedzone/V6B06KVZ0ZL9U5 with vpc: vpc-99999999',
        'Successfully associated zone: /hostedzone/D7JTQ7EDFFYOWN with vpc: vpc-99999999'
    ]
    
### Testing

Before commiting changes, be sure to run the test suite:

    tox

### Python 3 Compatibility

This tool is compatible with **python 3.5+**.

The [tox](http://tox.readthedocs.io/en/latest/index.html) library is used to run tests with multiple python versions. To run these tests, first ensure that all supported python versions are installed locally. Then, simply run:

    tox