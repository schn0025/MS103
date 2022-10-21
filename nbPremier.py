from pygame import*
from yapf import*
from isort import*
from flake8 import*
from bandit import*
from mypy import*
from unittest import*
from sphinx import*

def nbPremier(n:int)->list:
    """
    parametre:
        n: nopmbre de premier voulu 
    retour:
        lst: liste de n nombre premier
    """
    lst=[]
    lst1=[]
    for i in range(2,n):
        lst.append(i)
    nbList=1
    while len(lst1)<n:
        lst1.append(lst.pop(0))
        i=0
        if lst!=[]:
            while i!=len(lst):
                if lst[i]%lst1[-1]==0:
                    lst.pop(i)
                else:
                    i+=1
        else:
            nbList+=1
            for i in range(n*(nbList-1),n*nbList):
                lst.append(i)
            for elt in lst1:
                curs=0
                while curs<len(lst):
                    if lst[curs]%elt==0:
                        lst.pop(curs)
                    else:
                        curs+=1

    return lst1
print(nbPremier(10))
