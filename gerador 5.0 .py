import json

arquivo = input('Digite o nome do arquivo .json (sem o .json) \n')+str('.json')

with open(f'JSON/{arquivo}', encoding='utf-8') as f:
    dados = json.load(f)

n = int(input('Digite o número de estruturas: '))
b = str(' ')
pathway = input('''Insira o nome do Arquivo HTML aqui (minusculas, 
sem caracteres especiais, apens letras e -(traços): ''')+str('.html')
file = open('site/paginas/'+pathway, 'w')

file.write("""
{% extends 'master.html' %}
{% block style%}
  @media (max-width: 768px) {
    .general{
        margin-top: 100px;
        display: flex;
        justify-content: center;
    }
  }
  .general{
    margin-top: 120px;
    display: flex;
    justify-content: center;

  }
  .container{
        display: flex;
        Flex-direction: row;
        flex-wrap: wrap;
        position: relative;
        justify-content: center;
        padding: 30px 20px;
        background-color: rgb(255, 255, 255);
        border-radius: 30px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.2);             
  }
  .content1{
    padding: 15px 50px;
    flex: content;
    justify-content: space-between;
  }
    .container img {
        max-width: 800px;
        border-radius: 16px;
        object-fit: contain;
    }
    .low-image{
        display: inline-block;
        position: relative;
    }
    #fullImage {
        filter: blur(0px);
    }
    .mask{
        visibility: hidden;
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
        cursor: pointer;
        filter: drop-shadow(-5px 10px 5px black);
    }
    .showMask{
        visibility: visible;
    }
    .content2{
        background-color: #f1f1f1;
        max-height: 0;
        overflow: hidden;
        border-radius: 0px 0px 16px 16px;
        transition: max-height 0.2s ease-out;
    }
    .content2 form{
        padding: 20px;
    }
    .content2 label{
        padding: 5px;
        display: inline-block;
    }
    .show{display: block;}

/*FOOTER*/
.footer-dark {
  margin-top: 40px;
  padding:50px 0;
  color:#f0f9ff;
  background-color:#282d32;
}
.footer-dark .row{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.row{
  --bs-gutter-x: 0rem;
}
.footer-dark .row .col{
  line-height:1.6;
  font-size:14px;
  margin: 15px;
  max-width:30%;
}

.footer-dark h3 {
  margin-top:0;
  margin-bottom:12px;
  font-weight:bold;
  font-size: 18px;
}

.footer-dark ul {
  padding:0;
  list-style:none;
  line-height:1.6;
  font-size:14px;
  margin-bottom:0;
}

.footer-dark ul a {
  color:inherit;
  text-decoration:none;
  opacity:0.6;
}

.footer-dark ul a:hover {
  opacity:0.8;
}
.footer-dark .copyright{
  margin-top: 30px;
  text-align: center;
}
.dados, .dados a{
  text-align: center;
  color: #f0f9ff;
  font-size:10px;
}
{% endblock style%}
{% block content%}
</style>
<div class="general">
    <div class="container">
        <div class="content1">
                <h2>""" + dados['h2'] + """</h2>
                <ul>
                <li>""" + dados['ul']['lamina'] + """</li>
                <li>""" + dados['ul']['corte'] + """</li>
                <li>""" + dados['ul']['aumento'] + """</li>
                <li>""" + dados['ul']['coloracao'] + """</li>
                </ul>
                <div class="accordion" id="accordionExample">
                  <div class="accordion-item">
                    <h2 class="accordion-header">
                      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" 
                      data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                        Menu de estruturas
                      </button>
                    </h2>
                    <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
                      <div class="accordion-body">
                      <div class="form-check form-switch">
                          <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault" onclick="toggle()">
                          <label class="form-check-label" for="flexSwitchCheckDefault"><strong>Desfoque</strong></label>
                        </div>
                        <form action="" id="dropdownfn" class="form-check">""")
# Checkboxloop
for c in range(1, n + 1):
    x = dados['estruturas']['e'+str(c)]['label']
    l = dados['estruturas']['e' + str(c)]['link']
    if l != str('') and l != str('#linkproximapag'):
        file.write("""\n                           <input class="form-check-input" type="checkbox" id=\"""" + str(c) + """_check\" name="fav_language" value="HTML"
                               onclick="check(\'""" + str(c) + """\')"><label for="html"><a href=\""""+l+"""\">""" + b + x + """</a></label><br>""".format(c, c))
    else:
        file.write("""\n                           <input class="form-check-input" type="checkbox" id=\"""" + str(c) + """_check\" name="fav_language" value="HTML"
                                       onclick="check(\'""" + str(
            c) + """\')"><label for="html">""" + b + x + """</label><br>""".format(c, c))
file.write("""\n                        </form>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="content2">
                    </div>
                    </div>
                        <div class="low-image">
                            <!--fullImage-->
                            <img src=\"""" + dados['estruturas']['fullImage']['src'] + """\" usemap="#map" id="fullImage">
                            <!--Mask-->
                            """)
# Mask loop
for c in range(1, n + 1):
    l = dados['estruturas']['e'+str(c)]['link']
    s = dados['estruturas']['e'+str(c)]['src']
    file.write('\n                            <a href=\"'+l+'\">'
                                '\n                               <img class="mask" id=\"'+ str(c)+'\" src=\"'+s+'\" alt=>'+
               '\n                            </a>')
file.write("""
                    </div>
                    <!--Image map -->
                    <div class="imagemap">
                        <map name="map">
                        """)
    # Imagemap loop
for c in range(1, n + 1):
    co = dados['estruturas']['e' + str(c)]['coords']
    li = dados['estruturas']['e' + str(c)]['link']
    xl = dados['estruturas']['e' + str(c)]['label']
    file.write('\n                           ''<area shape="poly" coords=\"' + co + '\"'
               '\n                           ''href=\"' + li + '\" alt=\"' + xl + '\">')
file.write("""</map>
            </div>
            </div>
        </div>
    </div>
<script>//Checkbox
    function check(id) {
        var checkBox = document.getElementById(id + "_check");
        var mask = document.getElementById(id);
        const element = document.querySelector('.mask');
        if (checkBox.checked == true) {
        mask.style.visibility = "visible";
        } else {
        mask.style.visibility = "hidden";
        }
    }
  </script>
<script>
    function toggle() {
        var checkBox = document.getElementById("flexSwitchCheckDefault");
        if (checkBox.checked == true) {
        document.getElementById("fullImage").style.filter = 'blur(3px)';
        mask.classList.add('animate__animated', 'animate__tada');
        } else {
        document.getElementById("fullImage").style.filter = 'blur(0px)';
        }
    }
</script>
{% endblock content%}
""")

file.close()
print(f'Your HTML file was scripted! Check {pathway} to see it!')
