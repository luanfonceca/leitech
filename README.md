Projeto LeiTech
=======
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">Leitech</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/Leitech/leitech" property="cc:attributionName" rel="cc:attributionURL">Projeto Leitech</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/Leitech/leitech" rel="dct:source">https://github.com/Leitech/leitech</a>.

Como Instalar e Configurar
===============
1. Clone ou Baixe esse repositório;
2. Entre na pasta do projeto, onde se encontra os códigos:
    - `$ cd leitech/leitech`
3. Certifique-se de já ter o Python, na versão ~2.7, instalado. Instale o [pip](http://www.pip-installer.org/en/latest/) ou [easy_install](http://pythonhosted.org/distribute/easy_install.html);
4. Instale as dependências do projeto;
    - `$ pip install -r requirements.txt`
5. Copie o `.sample`, para o seu:
    - `cp settings_local.py.sample settings_local.py`
6. Configure o `DATABASES`, dentro do arquivo [settings_local](https://github.com/Leitech/leitech/blob/master/leitech/settings_local.py.sample#L20) file.
7. Sincronize o seu banco, com os Models e as Aplicações externas:
    - ```python manage.py syncdb --migrate```
8. Rode o seu projeto:
    - ```python manage.py runserver```
9. Veja ele rodando na `localhost`; 
    - ```127.0.0.1:8000```

- você pode mudar a  *porta* na qual o django rodará seu projeto: 
    - ```python manage.py runserver 8080``` --> ```127.0.0.1:8080```

Gerar Documentação do Código
===============
1. Clone ou Baixe esse repositório;
2. Entre na pasta do projeto, onde se encontra os códigos:
    - `$ cd leitech/leitech`
3. Use o comando `autodocs` para gerar as páginas html:
    - `$ python manage.py autodocs`
4. Acesse a pasta e abra em seu navegador o arquivo `index.html`:
    - `$ open ../docs/doc_code/index.html`
