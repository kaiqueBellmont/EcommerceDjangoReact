### Como rodar (temporário)
# TEMPORÁRIO:
- Tenha o python 3.8^ instalado em seu computador. 
- Node.Js

Basta clonar o projeto em qualquer diretório:
<br>
- `Na Raiz do projeto:`
- `cd EcommerceDjangoReact/backend`
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py createsuperuser && python manage.py migrate && python manage.py runserver`


### em outro terminal:
- `Na Raiz do projeto:`
- `cd backend/frontend  && npm install --legacy-peer-deps && npm start`

### o Projeto irá rodar nas portas 3000 (front) e 8000 (back)
#### o docker está funciionando, mas está dando um erro de proxy, que resolverei em breve.

- O projeto estava deployado todo na amazon, mas encerrei a minha conta temporariamente por custos.
- O Front estava no AWS amplify, o back no EBs (instância do ec2)
- o banco era o AWS RDS e os arquivos estáticos estavam em um bucket.

- Em breve eu terminarei o refactor do projeto, os testes e a documentação.
- Na Raiz do projeto back (localhost/8000), pode-se ver um pouco do swagger.
- Alguns testes feitos com o comando: <br>
- (raiz) `cd backend/ && pytest`
- Farei a refatoração pytonica, peps, types, etc.
- Voltarei com o projeto para a amazon.
- Atualizarei o front, já que utilizei bastante coisa que já está bem antigo.
- terminarei os testes e a documentação.

### Este projeto é totalmente coltado para fins estudantis.
### Eu quis fazer um projeto inteiro sozinho, back, front, testes, documentação, deploy, etc.
#### Ainda não está terminado, está cerca de 70%. (Está funcionando, mas falta muito ainda.)
