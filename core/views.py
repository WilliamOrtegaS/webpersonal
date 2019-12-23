from django.shortcuts import render, HttpResponse
html_base ="""
<h1>Mi web Personal</h1>
<ul>
    <li><a  style="text-decoration: none;" href="/">Portada</a></li>
    <li><a  style="text-decoration: none;" href="/about-me/">Acerca de</a></li>
    <li><a  style="text-decoration: none;" href="/portfolio/">Portafolio</a></li>
    <li><a  style="text-decoration: none;" href="/contact/">Contacto</a></li>
</ul>
"""

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
    #html =  '<h1>WEB</h1>'
    #for x in range(10):
    #    html += '<h2>Soy willy</h2>'
    #return HttpResponse(html_base+""" 
    #    <h2>Portada</h2>
    #    <p>Esto es la protada</p>
    #""")

def about(request):
    return render(request, 'core/about.html')
##    return HttpResponse(html_base+""" 
##        <h2>Acerca de</h2>
##        <p>Soy un aprendiz</p>
##    """)

#def portafolio(request):
#    return render(request, 'core/portfolio.html')
#    return HttpResponse(html_base + """ 
#        <h2>Portafolio</h2>
#        <p>Bienvenido a portafolio</p>
#    """)

def contacto(request):
    return render(request, 'core/contact.html')
    #return HttpResponse(html_base + """ 
    #    <h2>Contacto</h2>
    #    <p>Bienvenido a Contactos</p>
    #""")