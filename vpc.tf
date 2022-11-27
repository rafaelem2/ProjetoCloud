resource "aws_vpc" "main" {
  for_each = toset(var.vpc_name)
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = each.value
  }
}

resource "aws_subnet" "subnet" {
  for_each = toset(var.vpc_name)
  vpc_id            = aws_vpc.main[each.value].id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "Public Subnet"
  }
}

resource "aws_internet_gateway" "ig" {
  for_each = toset(var.vpc_name)
  vpc_id = aws_vpc.main[each.value].id

  tags = {
    Name = "Internet Gateway"
  }
}