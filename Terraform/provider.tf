terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "5.7.0"
    }
  }

  backend "s3" {
    bucket = "NEEDS TO BE UPDATED WITH INITIAL BUCKET NAME"
    key = "cicdexample/tfstate"
    region = "eu-west-2"
  }
}

provider "aws" {
    region = "eu-west-2"
}