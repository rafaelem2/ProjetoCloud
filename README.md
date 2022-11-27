# Projeto Cloud - AWS e Terraform

* Rafael Monteiro

O objetivo desse projeto é desenvolver uma aplicação capaz de provisionar uma infraestrutura por meio do terminal para gerenciar e administrá-la (construir, alterar e deletar recursos).

## Tutorial de Instalação e Operação

É recomendado a criação de um ambiente virtual Python:

```
python -m venv venv
```


- Instalação do Terraform

Para saber como instalar o Terraform no seu Sistema Operacional, entre no link a seguir:[Terraform](https://developer.hashicorp.com/terraform/downloads).

- AWS CLI

Configurando AWS para usar o Terraform. Isso deve ser feito a partir da [AWS Command Line Interface](https://aws.amazon.com/pt/cli/).

Nesse passo devem ser inseridas as IAM credentials (Access Key e Secret Access Key) para autenticar o Terraform AWS provider. **Lembre-se de não compartilhar tais informações e torná-las públicas.**

## Executando aplicação

Para executar a aplicação utilize:

```
python projeto.py
```

A aplicação inicia na tela do menu principal e dá opção de escolher entre os diversos serviços que ela oference.

Cada opção pode ser selecionada digitando o número correspondente:

    1. Criar instância
    Permite que o usuário crie uma instânica podendo escolher o nome e o tipo. Além disso, caso exista algum security group, o usuário pode associá-lo com a instânica.
    2. Deletar instância
    Permite que o usuário delete a instância pelo nome.
    3. Criar VPC
    Permite que o usuário crie uma vpc podendo escolher o nome. Além de uma subnet e um internet gateway.
    4. Criar User
    Permite a criação de um usuário podendo escolher o nome.
    5. Deletar User
    Permite que o usuário seja deletado pelo nome.
    6. Criar Security Group
    Permite a criação de um Security Group podendo escolher o nome.
    7. Deletar Security Group
    Permite que o Security Group seja deletado pelo nome.
    8. Listar
    Listar todas instâncias e suas regiões, usuários, grupos de segurança e suas regras.
    9. Sair
    Fecha a aplicação.
    10. Deleta tudo
    Deleta tudo o que foi criado pelo usuário.
