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
    djtext = request.POST.get("text", "none")
    # From index.html by using name="removepunc" we transfer data from checkbox input  to  option_button
    removepunc = request.POST.get("removepunc", "off")
    # From index.html by using name="capitalize" we transfer data from checkbox input  to  capitalize
    capitalize = request.POST.get("capitalize", "off")
    # Capitalize the content of djtext
    newlineremover = request.POST.get("newlineremover", "off")

    sremove = request.POST.get("sremove", "off")

    charcount = request.POST.get("charcount", "off")

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
        # params = {'purpose': purpose, 'analysed_text': analysed}
        # return render(request, "analyse.html", params)
        djtext = analysed

    if capitalize == "on":
        analysed = ""
        purpose = "Making Upper Case !!!"
        for char in djtext:
            analysed = analysed + char.upper()
        print("Analysed Text : ", analysed)
        # params = {'purpose': purpose, 'analysed_text': analysed}
        # return render(request, "analyse.html", params)
        djtext = analysed

    if newlineremover == "on":
        analysed = ""
        for char in djtext:
            if char != "\n":
                analysed = analysed + char
        purpose = "Removing New Line"
        # params = {'purpose': purpose, 'analysed_text': analysed}
        # return render(request, "analyse.html", params)
        djtext = analysed

    if sremove == "on":
        analysed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analysed = analysed + char

        purpose = "Removing New Line"
        # params = {'purpose': purpose, 'analysed_text': analysed}
        # return render(request, "analyse.html", params)
        djtext = analysed

    if charcount == "on":
        analysed = len(djtext)
        print(analysed)
        purpose = "Counting Characters "
        params = {"purpose": purpose, "analysed_text": analysed}
        return render(request, "charcount.html", params)

    

    params = {'purpose': purpose, 'analysed_text': djtext}
    return render(request, "analyse.html", params)
