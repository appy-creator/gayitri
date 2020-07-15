import os
from django.shortcuts import render
from os import listdir
# Create your views here.
def home1_view(request):
    return render(request,'home1.html',{})

def About1_view(request):
    return render(request,'About1.html',{})

def Abs_summarize(request):
    Path = './static/dataset/Abs_summarize'
    lis = [folder for folder in listdir(Path)]
    params = {'List_of_dirs':lis,'dataset':'Abs_summarize'}
    return render(request,'dataset.html',params)
def Ext_summarize(request):
    Path = './static/dataset/Ext_summarize'
    lis = [folder for folder in listdir(Path)]
    params = {'List_of_dirs':lis,'dataset':'Ext_summarize'}
    return render(request,'dataset.html',params)
def ODQA_dataset(request):
    Path = './static/dataset/ODQA_dataset'
    lis = [folder for folder in listdir(Path)]
    params = {'List_of_dirs':lis,'dataset':'ODQA_dataset'}
    return render(request,'dataset.html',params)
def SQuAD_dataset(request):
    Path = './static/dataset/SQuAD_dataset'
    lis = [folder for folder in listdir(Path)]
    params = {'List_of_dirs':lis,'dataset':'SQuAD_dataset'}
    return render(request,'dataset.html',params)

"""
def detail(request,article_id):
    Path = "./static/dataset/Abs_summerize/"+article_id+"/"
    lis = [folder for folder in listdir(Path)]
    first = lis[0]
    org_article = os.path.join(Path,first)+"/article."+first+".txt"
    sum_article = os.path.join(Path,first)+"/article."+first+".summ.txt"

    f = open(org_article,"r",encoding="utf-8")
    org_content = f.read()
    f.close()

    f = open(sum_article,"r",encoding="utf-8")
    sum_content = f.read()
    f.close()

    content = {
        'article' : org_content,
        'summary' : sum_content,
        'base_url': Path,
        'folder' : article_id,
        'active' : lis[0],
        'list_folders' : lis,
    }
    return render(request, 'articles.html',content)
"""
def ContactUs1_view(request):
    return render(request,'ContactUs1.html',{})

def Help1_view(request):
    return render(request,'Help1.html',{})

def get_articles(request,dataset,folder_path):
	path="./static/dataset/"+dataset+"/"+folder_path+"/"
	if(dataset=="Abs_summarize"):
		lis=[folder for folder in listdir(path)]
	elif(dataset=="Ext_summarize"):
		lis=[folder.split('.')[0] for folder in listdir(path+"input")]
	elif(dataset=="ODQA_dataset"):
		lis=[folder for folder in listdir(path)]
	elif(dataset=="SQuAD_dataset"):
		lis=[folder for folder in listdir(path)]
	else:
		return render(request,'error.html',{"error":"The dataset path is specified"})
	content={
	    'folder' : folder_path,
	    'list_folders' : lis,
	    'dataset' : dataset,
	}
	return render(request,'articles.html',content)

def get_contents(request,dataset,folder_path,article):
	path="./static/dataset/"+dataset+"/"+folder_path+"/"
	if(dataset=="Abs_summarize"):
		lis=[folder for folder in listdir(path)]
	elif(dataset=="Ext_summarize"):
		lis=[folder.split('.')[0] for folder in listdir(path+"input")]
	elif(dataset=="ODQA_dataset"):
		lis=[folder for folder in listdir(path)]
	elif(dataset=="SQuAD_dataset"):
		lis=[folder for folder in listdir(path)]
	else:
		return render(request,'error.html',{"error":"The dataset path is specified"})
	org_article=sum_article=""
	if(dataset=="Abs_summarize"):
		org_article=os.path.join(path,article)+"/article."+article+".txt"
		sum_article=os.path.join(path,article)+"/article."+article+".summ.txt"
	elif(dataset=="Ext_summarize"):
		org_article=path+"/input/"+article+".txt"
		sum_article=path+"/output/"+article+"_out.txt"
	elif(dataset=="ODQA_dataset"):
		org_article=os.path.join(path,article)+"/article."+article+".txt"
		sum_article=os.path.join(path,article)+"/article."+article+".summ.txt"
	elif(dataset=="SQuAD_dataset"):
		org_article=os.path.join(path,article)+"/article."+article+".txt"
		sum_article=os.path.join(path,article)+"/article."+article+".summ.txt"
	else:
		return render(request,'error.html',{"error":"The dataset path is specified"})

	f=open(org_article,"r",encoding="utf-8")
	org_content=f.read()
	f.close()

	f=open(sum_article,"r",encoding="utf-8")
	sum_content=f.read()
	f.close()

	content={
	    'article_id':article,
	    'article':org_content,
	    'summary':sum_content,
	    'folder':folder_path,
	    'list_folders':lis,
	    'dataset':dataset,
	}
	return render(request,'articles.html',content)

