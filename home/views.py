from django.shortcuts import render_to_response, render, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from authentico.models import User
import feedparser
# import xlrd, unicodedata'
import pandas as pd


def supno(request):
    if request.POST:
        aranan = request.POST["aranan"]

        df = pd.read_excel("yeni.xlsx", "Sayfa1")
        # for i in df.index:
        #     if df["Supplier No."][i] == aranan:

        # result = df.loc[df['Supplier No.'] == aranan]
        result = df.loc[df['Supplier No.'].isin(['991571'])]
        supplier_no = result[result.columns[0]].values[0]
        name = result[result.columns[1]].values[0]
        product_manager = result[result.columns[2]].values[0]
        turnover1 = result[result.columns[3]].values[0]
        turnover2 = result[result.columns[4]].values[0]
        turnover3 = result[result.columns[5]].values[0]
        turnover4 = result[result.columns[6]].values[0]

        c = {"request": request,
             "supplier_no": int(supplier_no),
             "name": name,
             "product_manager": product_manager,
             "turnover1": int(turnover1),
             "turnover2": int(turnover2),
             "turnover3": int(turnover3),
             "turnover4": int(turnover4)}

        c.update(csrf(request))

        return render(request, "result/excel.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "makequery/excel.html", c)


def year(request):
    if request.POST:
        aranan = request.POST["yearselect"]

        df = pd.read_excel("yeni.xlsx", "Sayfa1")

        if aranan == '2015':
            turnover = df[df.columns[3]].tolist()
        elif aranan == '2016':
            turnover = df[df.columns[4]].tolist()
        elif aranan == '2017':
            turnover = df[df.columns[5]].tolist()
        elif aranan == '2018':
            turnover = df[df.columns[6]].tolist()

        # supplier_no = result[result.columns[0]].values[0]
        # name = result[result.columns[1]].values[0]
        # product_manager = result[result.columns[2]].values[0]
        # turnover1 = result[result.columns[3]].values[0]
        # turnover2 = result[result.columns[4]].values[0]
        # turnover3 = result[result.columns[5]].values[0]
        # turnover4 = result[result.columns[6]].values[0]

        c = {"request": request,
             "turnover": turnover}

        c.update(csrf(request))

        return render(request, "result/excel-date.html", c)

    c = {"request": request}
    c.update(csrf(request))

    return render(request, "makequery/excel-date.html", c)


def detayli(request):
    df = pd.read_excel("yeni.xlsx", "Sayfa1")
    a = df[df.columns[3]].tolist()

    b = df[df.columns[4]].tolist()

    c = df[df.columns[5]].tolist()

    d = df[df.columns[6]].tolist()

    # supplier_no = result[result.columns[0]].values[0]
    # name = result[result.columns[1]].values[0]
    # product_manager = result[result.columns[2]].values[0]
    # turnover1 = result[result.columns[3]].values[0]
    # turnover2 = result[result.columns[4]].values[0]
    # turnover3 = result[result.columns[5]].values[0]
    # turnover4 = result[result.columns[6]].values[0]

    c = {"request": request,
         "a": a,
         "b": b,
         "c": c,
         "d": d}

    c.update(csrf(request))

    return render_to_response("result/detayli.html", c)


def all(request):
    df = pd.read_excel("yeni.xlsx", "Sayfa1")
    a = df[df.columns[3]].tolist()

    b = df[df.columns[4]].tolist()

    c = df[df.columns[5]].tolist()

    d = df[df.columns[6]].tolist()

    # supplier_no = result[result.columns[0]].values[0]
    # name = result[result.columns[1]].values[0]
    # product_manager = result[result.columns[2]].values[0]
    # turnover1 = result[result.columns[3]].values[0]
    # turnover2 = result[result.columns[4]].values[0]
    # turnover3 = result[result.columns[5]].values[0]
    # turnover4 = result[result.columns[6]].values[0]

    c = {"request": request,
         "a": a,
         "b": b,
         "c": c,
         "d": d}

    c.update(csrf(request))

    return render_to_response("result/all.html", c)


def name(request):
    if request.POST:
        aranan = request.POST["nameselect"]

        df = pd.read_excel("yeni.xlsx", "Sayfa1")
        result = df.loc[df['Name'].isin([aranan])]

        supplier_no = result[result.columns[0]].values[0]
        name = result[result.columns[1]].values[0]
        product_manager = result[result.columns[2]].values[0]
        turnover1 = result[result.columns[3]].values[0]
        turnover2 = result[result.columns[4]].values[0]
        turnover3 = result[result.columns[5]].values[0]
        turnover4 = result[result.columns[6]].values[0]

        c = {"request": request,
             "supplier_no": int(supplier_no),
             "name": name,
             "product_manager": product_manager,
             "turnover1": int(turnover1),
             "turnover2": int(turnover2),
             "turnover3": int(turnover3),
             "turnover4": int(turnover4)}

        c.update(csrf(request))

        return render(request, "result/excel.html", c)

    df = pd.read_excel("yeni.xlsx", "Sayfa1")
    names = df[df.columns[1]]

    c = {"request": request,
         "names": names}

    c.update(csrf(request))

    return render(request, "makequery/excel-name.html", c)


# # def query(request, id):
# #     df = pd.read_excel("yeni.xlsx", "Sayfa1")
# #     # for i in df.index:
# #     #     if df["Supplier No."][i] == aranan:
# #
# #     result = df.iloc[int(id)]
# #
# #     supplier_no = result[result.columns[0]].values[0]
# #     name = result[result.columns[1]].values[0]
# #     product_manager = result[result.columns[2]].values[0]
# #     turnover1 = result[result.columns[3]].values[0]
# #     turnover2 = result[result.columns[4]].values[0]
# #     turnover3 = result[result.columns[5]].values[0]
# #     turnover4 = result[result.columns[6]].values[0]
# #
# #     c = {"request": request,
# #          "supplier_no": int(supplier_no),
# #          "name": name,
# #          "product_manager": product_manager,
# #          "turnover1": int(turnover1),
# #          "turnover2": int(turnover2),
# #          "turnover3": int(turnover3),
# #          "turnover4": int(turnover4)}
# #
# #     c.update(csrf(request))
#
#     return render(request, "sonuc/excel.html", c)