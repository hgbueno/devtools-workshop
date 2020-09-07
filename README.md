# AWS BlackBelt | DevOps
***Workshop AWS DevTools***


## 1. Preparação

### 1.1 Valide o acesso à sua conta no EventEngine através da console.
*informações enviadas por e-mail* <br />
> * [Event Engine](https://dashboard.eventengine.run/login)

### 1.2 Caso ainda não tenha, instale a ***aws cli*** e crie um novo profile para a sua conta.
> * [Como instalar](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html)
> * [Como configurar](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

### 1.3 Valide a configuração do seu profile.
O comando abaixo deverá retornar seu **AccountId**:
```
aws sts get-caller-identity --query Account --output text --profile <profile>
```

### 1.4 Crie seu usuário para o CodeCommit.
* Crie um grupo chamado CodeCommitUsers e selecione a managed policy ***AWSCodeCommitPowerUser***.
* Crie um novo usuário com acesso do tipo ***Programmatic access*** (sem acesso à console) e o adicione ao grupo criado anteriormente.
* Crie uma nova credencial HTTPS para o CodeCommit para este novo usuário.

> * [Criação de um usuário do IAM na sua conta da AWS](https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/id_users_create.html#id_users_create_console)
> * [Configuração para usuários de HTTPS usando credenciais do Git](https://docs.aws.amazon.com/pt_br/codecommit/latest/userguide/setting-up-gc.html)


### 1.5 Confirme se a nova credencial está funcionando.
* Crie um repositório apenas para teste.
* Clone o repositório em sua máquina utilizando a nova credencial.
* Delete o repositório.

> [Conceitos básicos do Git e do AWS CodeCommit](https://docs.aws.amazon.com/pt_br/codecommit/latest/userguide/getting-started.html#getting-started-create-repo)


### 6. Clone este repositório.
```
git clone https://github.com/hgbueno/devtools-workshop.git
```


## 2. Criação das stacks de fundação
> Seguindo a boa prática de segmentar stacks em camadas, criaremos 3 stacks:
> * ***1. Netwoking:*** Toda a infraestrutura de VPC e conectividade em multi-az (2), incluindo o Application Load Balancer.
> * ***2. Common:*** Recursos que serão compartilhados entre todas os micro-serviços que criaremos. KMS e S3 Bucket.
> * ***3. Fargate:*** Cluster Fargate.

### 2.1 Networking
```
 aws cloudformation deploy \
    --stack-name networking \
    --template-file templates/networking.yaml \
    --capabilities CAPABILITY_IAM \
    --region <region> \
    --profile <profile>
```

### 2.2 Commons
```
aws cloudformation deploy \
    --stack-name commons \
    --template-file templates/commons.yaml \
    --capabilities CAPABILITY_IAM \
    --region <region> \
    --profile <profile>
```

### 2.3 Fargate
```
aws cloudformation deploy \
    --stack-name fargate \
    --template-file templates/fargate.yaml \
    --capabilities CAPABILITY_IAM \
    --region <region> \
    --profile <profile>
```

## 3. Criação o primeiro micro-serviço


### 3.1 Crie a stack para o micro-serviço
* Através da console Web do Cloudformation, crie uma nova stack com base no template **pipeline.yaml** com os seguintes parâmetros:
    * Stack name: myapp
    * ServiceName: myapp
    <br />
    *Não é necessário alterar os valores dos demais parâmetros.*

* Verifique se a pipeline foi criada no CodePipeline.
* Verifique se o repositório foi criado no CodeCommit.

### 3.2 Clone o novo repositório e copie os arquivos da aplicação.
* Clone o repositório
<br />
Acesse seu repositório do CodeCommit pela console web, clique em **Clone URL**, depois em **Clone HTTPS**.
Na sua máquina, execute:
```
git clone <RepoURL>
```
* Copie o conteúdo do diretório sample-app do repositório do workshop para o novo repositório do CodeCommit.
Exemplo:

```
cp -rpf ../devtools-workshop/sample-app/* <RepoName>/
```
* Edite os seguintes arquivos para o novo micro-serviço:
    * templates/service.yaml
        * ServiceName: myapp
        * ServicePath: myapp/
        * BranchName: myapp
        * ContainerPort: 5000
        * AlbRulePriority: 2

    * app/main.py
        *  **@app.route("/myapp")**

* Envie as mudanças para repositório
```
git add .
git commit -m "first commit"
git push origin master
```