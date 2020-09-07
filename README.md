# Workshop AWS DevTools
## AWS BlackBelt | DevOps


----

### **Preparação**

1. Valide o acesso à sua conta no EventEngine através da console.
*informações enviadas por e-mail*
https://dashboard.eventengine.run/login

2. Instale a ***aws cli*** e crie um novo profile para a sua conta.
* Como instalar: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html
* Como configurar: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

3. Valide a configuração do seu profile.
* O comando abaixo deverá retornar seu AccountId:
```bash
aws sts get-caller-identity --query Account --output text --profile <profile>
```

4. Clone este repositório.
```
git clone https://github.com/hgbueno/devtools-workshop.git
```
----

### **Criação das Stacks de fundação**
Seguindo a boa prática de segmentar stacks em camadas, criaremos 3 stacks:
1. Netwoking: Toda a infraestrutura de VPC e conectividade em multi-az (2), incluindo o Application Load Balancer.

2. Common: Recursos que serão compartilhados entre todas os micro-serviços que criaremos. KMS e S3 Bucket.

3. Fargate: Cluster Fargate.


**1. Networking**
```
 aws cloudformation deploy \
    --stack-name networking \
    --template-file templates/networking.yaml \
    --capabilities CAPABILITY_IAM \
    --region <region> \
    --profile <profile>
```

**2. Common**
```
aws cloudformation deploy \
    --stack-name common \
    --template-file templates/common.yaml \
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
