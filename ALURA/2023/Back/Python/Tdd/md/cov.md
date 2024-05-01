pip install pytest-cov==3.0.0

pytest --cov

pytest --cov=bin tests

pytest --cov=bin tests --cov-report term-missing

    ---------- coverage: platform linux, python 3.10.6-final-0 -----------
    Name              Stmts   Miss  Cover   Missing
    -----------------------------------------------
    bin/bytebank.py      40      2    95%   16, 59 #Column,Line
    -----------------------------------------------
    TOTAL                40      2    95%



pytest --cov=bin tests --cov-report html
[]