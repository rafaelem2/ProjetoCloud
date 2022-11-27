import os
import json


def create_instance():
    name = input("Digite o nome da instância: ")
    print ("\nmicro \nsmall \nmedium \nlarge\n")
    type = input("Digite um dos tipos acima:\n")
    subnet = None
    sg = None
    sg = escolher_sg(sg)
    #subnet = escolher_subnet(subnet)
    #print(subnet)
    with open("variables.tf.json", 'r') as fp:
        variable = json.load(fp)
    variable["variable"]["instance_name"]["default"].append(name)
    variable["variable"]["instance_type"]["default"].append("t2."+type)
    if sg == None:
        variable["variable"]["instance_sg"]["default"].append(sg)
    else:
        variable["variable"]["instance_sg"]["default"].append([sg])

    #variable["variable"]["instance_subnet"]["default"].append(subnet)
    
    with open("variables.tf.json", 'w') as fp:
        json.dump(variable, fp, indent=4)
    os.system("terraform init ") # Inicializa o Terraform      
    os.system(" terraform apply -auto-approve") # Aplica as configurações do Terraform

def delete_instance():
    with open("variables.tf.json", 'r') as fp:
        variable = json.load(fp)
    print("Instâncias disponíveis: ")
    for i in range(len(variable["variable"]["instance_name"]["default"])):
        print(i, " - ", variable["variable"]["instance_name"]["default"][i], " - ", variable["variable"]["instance_type"]["default"][i])
    option = input("Escolha uma instância para deletar: ")
    del variable["variable"]["instance_name"]["default"][int(option)]
    del variable["variable"]["instance_type"]["default"][int(option)]
    del variable["variable"]["instance_sg"]["default"][int(option)]
    with open("variables.tf.json", 'w') as fp:
        json.dump(variable, fp, indent=4)
    os.system("terraform init ") # Inicializa o Terraform
    os.system(" terraform apply -auto-approve") # Aplica as configurações do Terraform

def delete_security_group():
    with open("variables.tf.json", 'r') as fp:
        variable = json.load(fp)
    print("Security Groups disponíveis: ")
    for i in range(len(variable["variable"]["sg_name"]["default"])):
        print(i, " - ", variable["variable"]["sg_name"]["default"][i])
    option = input("Escolha um Security Group para deletar: ")
    del variable["variable"]["sg_name"]["default"][int(option)]
    with open("variables.tf.json", 'w') as fp:
        json.dump(variable, fp, indent=4)
    os.system("terraform init ") # Inicializa o Terraform
    os.system(" terraform apply -auto-approve") # Aplica as configurações do Terraform

def delete_user():
    with open("variables.tf.json", 'r') as fp:
        variable = json.load(fp)
    print("Usuários disponíveis: ")
    for i in range(len(variable["variable"]["user_name"]["default"])):
        print(i, " - ", variable["variable"]["user_name"]["default"][i])
    option = input("Escolha um usuário para deletar: ")
    del variable["variable"]["user_name"]["default"][int(option)]
    with open("variables.tf.json", 'w') as fp:
        json.dump(variable, fp, indent=4)
    os.system("terraform init ") # Inicializa o Terraform
    os.system(" terraform apply -auto-approve") # Aplica as configurações do Terraform
    
def create_vpc():
    name = input("Digite o nome da VPC: ")
    with open("variables.tf.json", 'r') as fp:
        variable = json.load(fp)
    variable["variable"]["vpc_name"]["default"].append(name)
    with open("variables.tf.json", 'w') as fp:
        json.dump(variable, fp, indent=4)
    os.system("terraform init ")
    os.system(" terraform apply -auto-approve")

def create_user():
    name = input("Digite o nome do usuário: ")
    with open("variables.tf.json", 'r') as fp:
        variable = json.load(fp)
    variable["variable"]["user_name"]["default"].append(name)
    with open("variables.tf.json", 'w') as fp:
        json.dump(variable, fp, indent=4)
    os.system("terraform init ")
    os.system(" terraform apply -auto-approve")

def create_sg():
    name = input("Digite o nome do Security Group: ")
    with open("variables.tf.json", 'r') as fp:
        variable = json.load(fp)
    variable["variable"]["sg_name"]["default"].append(name)
    with open("variables.tf.json", 'w') as fp:
        json.dump(variable, fp, indent=4)
    os.system("terraform init ")
    os.system(" terraform apply -auto-approve")

def list_instances():
    with open("terraform.tfstate", 'r') as fp:
        variable = json.load(fp)
    for i in range(len(variable["resources"])): 
        if variable["resources"][i]["type"] == "aws_instance":
            print("\nLISTA DE INSTÂNCIAS:")
            for j in range(len(variable["resources"][i]["instances"])):
                print(variable["resources"][i]["instances"][j]["attributes"]["tags"]["Name"], " - ", variable["resources"][i]["instances"][j]["attributes"]["instance_type"])
        if variable["resources"][i]["type"] == "aws_vpc":
            print("\nLISTA DE VPCs:")
            for j in range(len(variable["resources"][i]["instances"])):
                print(variable["resources"][i]["instances"][j]["attributes"]["tags"]["Name"])
        if variable["resources"][i]["type"] == "aws_iam_user":
            print("\nLISTA DE USUÁRIOS:")
            for j in range(len(variable["resources"][i]["instances"])):
                print(variable["resources"][i]["instances"][j]["attributes"]["name"])
        if variable["resources"][i]["type"] == "aws_security_group":
            print("\nLISTA DE SECURITY GROUPS:")
            for j in range(len(variable["resources"][i]["instances"])):
                #print security group name id cidr port
                print(variable["resources"][i]["instances"][j]["attributes"]["name"], " - ", variable["resources"][i]["instances"][j]["attributes"]["id"], " - ", variable["resources"][i]["instances"][j]["attributes"]["ingress"][0]["cidr_blocks"][0], " - ", variable["resources"][i]["instances"][j]["attributes"]["ingress"][0]["from_port"])
                

def escolher_sg(sg):
    with open("terraform.tfstate", 'r') as fp:
        variable = json.load(fp)    
    for i in range(len(variable["resources"])):
        if variable["resources"][i]["type"] == "aws_security_group":
            for j in range(len(variable["resources"][i]["instances"])):
                print (j+1, " - ", variable["resources"][i]["instances"][j]["attributes"]["name"], " - ", variable["resources"][i]["instances"][j]["attributes"]["id"])
            sg = input("Digite o indice do Security Group: ")
            for j in range(len(variable["resources"][i]["instances"])):
                if sg == str(j+1):
                    sg = variable["resources"][i]["instances"][j]["attributes"]["id"]
                else: 
                    sg = None
    
    return sg

def escolher_subnet(subnet):
    with open("terraform.tfstate", 'r') as fp:
        variable = json.load(fp)    
    for i in range(len(variable["resources"])):
        if variable["resources"][i]["type"] == "aws_subnet":
            for j in range(len(variable["resources"][i]["instances"])):
                print (j+1, " - ", variable["resources"][i]["instances"][j]["attributes"]["tags"]["Name"], " - ", variable["resources"][i]["instances"][j]["attributes"]["id"])
            subnet = input("Digite o indice da Subnet: ")
            for j in range(len(variable["resources"][i]["instances"])):
                if subnet == str(j+1):
                    subnet = variable["resources"][i]["instances"][j]["attributes"]["id"]
                else: 
                    subnet = None
        
    return subnet

def delete_all():
    os.system("terraform destroy -auto-approve")
    #deleta variaveis do arquivo variables.tf.json
    with open("variables.tf.json", 'r') as fp:
        variable = json.load(fp)
    variable["variable"]["instance_name"]["default"] = []
    variable["variable"]["instance_type"]["default"] = []
    variable["variable"]["vpc_name"]["default"] = []
    variable["variable"]["user_name"]["default"] = []
    variable["variable"]["sg_name"]["default"] = []
    variable["variable"]["instance_sg"]["default"] = []
    variable["variable"]["instance_subnet"]["default"] = []
    with open("variables.tf.json", 'w') as fp:
        json.dump(variable, fp, indent=4)
    

def main():
    while True:
        print("\n1 - Criar instância")
        print("2 - Deletar instância")
        print("3 - Criar VPC")
        print("4 - Criar User")
        print("5 - Deletar User")
        print("6 - Criar Security Group")
        print("7 - Deletar Security Group")
        print("8 - Listar")
        print("9 - Sair")
        print("10 - Deleta tudo")

        option = input("\nEscolha uma opção: ")
        if option == "1":
            create_instance()
        elif option == "2":
            delete_instance()
        elif option == "3":
            create_vpc()
        elif option == "4":
            create_user()
        elif option == "5":
            delete_user()
        elif option == "6":
            create_sg()
        elif option == "7":
            delete_security_group()
        elif option == "8":
            list_instances()
        elif option == "9":
            break
        elif option == "10":
            delete_all()
        else:
            print("Opção inválida")

main()