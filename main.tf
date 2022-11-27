terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-east-1"
}

resource "aws_instance" "app_server" {
  for_each = toset(var.instance_name)
  instance_type = var.instance_type[index(var.instance_name, each.value)]
  ami           = "ami-0ee23bfc74a881de5"
  vpc_security_group_ids = var.instance_sg[index(var.instance_name, each.value)]
  #subnet_id = var.instance_subnet[index(var.instance_name, each.value)]


  tags = {
    Name  = each.value
  }
}

