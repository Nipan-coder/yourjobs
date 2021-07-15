from django.shortcuts import render
from django.contrib import messages
from .models import User

# Create your views here.
def Home(request):
  data=User.objects.all()
  return render(request,'app/index.html',{'data':data})

def Post(request):
  if request.method=='GET':
      return render(request,'app/post.html')
  else:
    postData = request.POST
    jtitle = postData.get('title')
    cname = postData.get('cname')
    eto = postData.get('eto')
    efrom = postData.get('eform')
    sto = postData.get('sto')
    sfrom = postData.get('sform')
    location = postData.get('loc')
    dec = postData.get('dec')

    user = User(jtitle=jtitle,
                    cname=cname,
                    eto=eto,
                    efrom=efrom,
                    sto=sto,
                    sfrom=sfrom,
                    location=location,
                    dec=dec)
    user.save()

  return render(request,'app/post.html')


def scarch(request):
  
  searchh=request.GET['search']
  jtitle=User.objects.filter(jtitle__icontains=searchh)
  cname=User.objects.filter(cname__icontains=searchh)
  location=User.objects.filter(location__icontains=searchh)
  product = jtitle.union(cname, location)
  
  
  return render(request,'app/search.html',{'products':product})