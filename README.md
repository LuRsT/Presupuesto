# Presupuesto

Web-based personal budget forecasting application.


## Install

Once you have a Python virtualenv, run:

    cd /path/to/presupuesto
    pip install .
    manage syncdb    # Create the user account you'll use later on!

Now store your start balance in a file at the root of the branch; e.g.:

    echo "1234.56" > BALANCE.txt

This balance must be the final one at the end of the previous month.

## Use

Inside the virtualenv where presupuesto was installed, run:

    manage runserver


### Disclaimer: You're on your own

I created this application within a few hours and the only plans I have for it
is to change it whenever I need a new feature.

My spare time is quite limited, so I won't offer any form of support for this
software.

That being said, I'd be happy to apply patches.
