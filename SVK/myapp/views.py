from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
from . import preprocessing
from . import myfunctions as mf

def home(request):
    if request.method =="POST":
        file = request.FILES["database"]

        table = preprocessing.preprocessing(file)
        counts = mf.histograms(table)
        m_a,m_b,f_a,f_b = mf.gender_class(table)
        c_a,c_b,n_a,n_b = mf.problem_class(table)
        print(m_a)

        data = {

            "counts":counts,
            "m_a":m_a,
            "m_b":m_b,
            "f_a":f_a,
            "f_b":f_b,
            "c_a":c_a,
            "c_b":c_b,
            "n_a":n_a,
            "n_b":n_b

        }
    else:
        data = {
            "counts":[[5,1,5],[6,2]],

        }
    return render(request, 'index.html', data)
