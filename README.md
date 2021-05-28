This is a python program which will extract the 'products' from reponse object. 
It make use of two APIs:-
1) https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&amp;q=*&amp;rows=10&amp;start=0
2) https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&amp;q=*&amp;rows=10&amp;start=1

The libraries used in main.py file are:-
import json
import requests
import csv

Please, install it in your python system to run the main.py file.

On running main.py, after execution of the program to csv files will be generated in the same folder as of main.py.
First csv file will be for first API and name of the file is "Unbxd-2021-interns test_Yashwant_Singh_Waskel_0.csv".
Second csv file will be for second API and name of the file is "Unbxd-2021-interns test_Yashwant_Singh_Waskel_1.csv".

I have not merged the data of both API into a single csv file as by looking at the example of the APIs given, it shows that first API will give you first set of results and second API will give you another set of results. Therefore, I have assumed that I have to create to different csv file for different APIs. 
