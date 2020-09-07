# Workshop AWS DevTools
## AWS BlackBelt | DevOps


----

### **Preparação**

1. Valide o acesso à sua conta no EventEngine através da console.<br />
*informações enviadas por e-mail* <br />
* [Event Engine](https://dashboard.eventengine.run/login)

2. Instale a ***aws cli*** e crie um novo profile para a sua conta.
* [Como instalar](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html)
* [Como configurar](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

3. Valide a configuração do seu profile.
O comando abaixo deverá retornar seu AccountId:
```
aws sts get-caller-identity --query Account --output text --profile <profile>
```

4. Clone este repositório.
```
git clone https://github.com/hgbueno/devtools-workshop.git
```

5. Crie seu usuário para o CodeCommit.
    * Crie um grupo chamado CodeCommitUsers e selecione a managed policy ***AWSCodeCommitPowerUser***.
    * Crie um novo usuário com acesso do tipo ***Programmatic access*** (sem acesso à console) e o adicione ao grupo criado anteriormente.
    * Crie uma nova credencial HTTPS para o CodeCommit para este novo usuário.

> * [Criação de um usuário do IAM na sua conta da AWS](https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/id_users_create.html#id_users_create_console)
> * [Configuração para usuários de HTTPS usando credenciais do Git](https://docs.aws.amazon.com/pt_br/codecommit/latest/userguide/setting-up-gc.html)


6. Confirme se a nova credencial está funcionando.
    * Crie um repositório apenas para teste.
    * Clone o repositório em sua máquina utilizando a nova credencial.
    * Delete o repositório.

> [Conceitos básicos do Git e do AWS CodeCommit](https://docs.aws.amazon.com/pt_br/codecommit/latest/userguide/getting-started.html#getting-started-create-repo)

----

### **Criação das stacks de fundação**
> Seguindo a boa prática de segmentar stacks em camadas, criaremos 3 stacks:
> * ***1. Netwoking:*** Toda a infraestrutura de VPC e conectividade em multi-az (2), incluindo o Application Load Balancer.
> * ***2. Common:*** Recursos que serão compartilhados entre todas os micro-serviços que criaremos. KMS e S3 Bucket.
> * ***3. Fargate:*** Cluster Fargate.

<br />

**1. Networking**
```
 aws cloudformation deploy \
    --stack-name networking \
    --template-file templates/networking.yaml \
    --capabilities CAPABILITY_IAM \
    --region <region> \
    --profile <profile>
```

**2. Commons**
```
aws cloudformation deploy \
    --stack-name commons \
    --template-file templates/commons.yaml \
    --capabilities CAPABILITY_IAM \
    --region <region> \
    --profile <profile>
```
**3. Fargate**
```
aws cloudformation deploy \
    --stack-name fargate \
    --template-file templates/fargate.yaml \
    --capabilities CAPABILITY_IAM \
    --region <region> \
    --profile <profile>
```

----
