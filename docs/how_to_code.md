Fala gente, aqui vai um tutorial simples de como as coisas devem acontecer!
### Observações:
* Tudo que começar com `$` é um comando pra ser executado no Terminal;

## Atualizando o código Local
Para atualizar o código, **é recomendado que não se tenha nenhum arquivo editado, pois isso pode causar um Conflito**, utilizamos o comando `pull`.
Garantindo que o código está sem alterações locais:
```bash
$ git status
# On branch master
nothing to commit (working directory clean)
```

Atualizando o código:
Vamos considerar que temos um Branch, chamado `master`, então vamos atualizar o código do Master que está no Servidor para o Master local:
```bash
$ git pull origin master
From github.com:Leitech/leitech
 * branch            master     -> FETCH_HEAD
Already up-to-date.
```
Isso quer dizer que não há nenhum código novo no servidor, caso contrário ele irá atualizar e dizer os arquivos alterados.
Segue um exemplo de um `pull` com arquivos no servidor:
```bash
$ git pull origin master
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 2), reused 0 (delta 0)
Unpacking objects: 100% (4/4), done.
From github.com:Leitech/leitech
 * branch            master     -> FETCH_HEAD
Updating 6ac7362..dbe4374
Fast-forward
 docs/how_to_code.md |   51 +++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 51 insertions(+)
 create mode 100644 docs/how_to_code.md
```


## Commitando
Um Simples Commit:
```bash
$ git add caminho/do/arquivo.html caminho/do/outro/arquivo.py ...
$ git commit -m "Mensagem do Commit"
```
### Commitando & associando uma *Issue*
Assumindo que temos uma Issue com o ID 200:
```bash
$ git add caminho/do/arquivo.html caminho/do/outro/arquivo.py ...
$ git commit -m "Iniciando resolucao do problema da issue #200."
```
### Commitando & Fechando uma *Issue*
Assumindo que temos uma Issue com o ID 200, apenas é necessário adicionar o **fix #ID_DA_ISSUE** para fecha-la:
```bash
$ git add caminho/do/arquivo.html caminho/do/outro/arquivo.py ...
$ git commit -m "fix #200 - resolvendo o problema da issue."
```

## Enviando Código para o Servidor
Para se enviar os Commits para o `Github`, usamos o commando `Push`:
Assumindo que estamos enviando o código para o branch `master`.
```bash
$ git add caminho/do/arquivo.html caminho/do/outro/arquivo.py ...
$ git commit -m "fix #200 - resolvendo o problema da issue."
$ git push origin master
```
