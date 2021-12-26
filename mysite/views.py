# Created By SK
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def practice(request):
    return render(request, "prac.html")


def analyse(request):
    # getting the text
    # From index.html by using name="text" we transfer data from text area to djtext
    djtext = request.GET.get("text", "none")
    # From index.html by using name="removepunc" we transfer data from checkbox input  to  option_button
    removepunc = request.GET.get("removepunc", "off")
    # From index.html by using name="capitalize" we transfer data from checkbox input  to  capitalize
    capitalize = request.GET.get("capitalize", "off")
    # Capitalize the content of djtext
    newlineremover = request.GET.get("newlineremover", "off")

    sremove = request.GET.get("sremove", "off")

    charcount = request.GET.get("charcount", "off")

    print("Whole Text : ", djtext)
    print("Remove Punctuations : ", removepunc)
    print("UPPER : ", capitalize)
    # analysed=djtext
    if removepunc == "on":
        punctuations = '''.,:"><(){}[];\/!@#$$%?^&*_-=+'''
        analysed = ""
        purpose = "Remove Punctuations !!!"
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        print("Analysed Text : ", analysed)
        params = {'purpose': purpose, 'analysed_text': analysed}
        return render(request, "analyse.html", params)

    elif capitalize == "on":
        analysed = ""
        purpose = "Making Upper Case !!!"
        for char in djtext:
            analysed = analysed + char.upper()
        print("Analysed Text : ", analysed)
        params = {'purpose': purpose, 'analysed_text': analysed}
        return render(request, "analyse.html", params)

    elif newlineremover == "on":
        analysed = ""
        for char in djtext:
            if char != "\n":
                analysed = analysed + char
        purpose = "Removing New Line"
        params = {'purpose': purpose, 'analysed_text': analysed}
        return render(request, "analyse.html", params)

    elif sremove == "on":
        analysed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analysed = analysed + char

        purpose = "Removing New Line"
        params = {'purpose': purpose, 'analysed_text': analysed}
        return render(request, "analyse.html", params)

    elif charcount == "on":
        analysed = len(djtext)
        print(analysed)
        purpose = "Counting Characters "
        params = {"purpose": purpose, "analysed_text": analysed}
        return render(request, "charcount.html", params)

    else:
        purpose = "Dont Remove Punctuations !!!"
        params = {'purpose': purpose, 'analysed_text': djtext}
        return render(request, "analyse.html", params)
