variable "aws_region" {
  description = "AWS region where infrastructure will be deployed"
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Name of the project used for resource tagging"
  default     = "medical-volunteering"
}

variable "instance_type" {
  description = "EC2 instance type for application server"
  default     = "t3.micro"
}

variable "db_name" {
  description = "RDS MySQL database name"
  default     = "medical_db"
}

variable "db_username" {
  description = "RDS database admin username"
  default     = "admin"
}

variable "db_password" {
  description = "RDS database password"
  sensitive   = true
}

variable "ami_id" {
  description = "Ubuntu AMI ID for EC2 instance in ap-south-1"
  default     = "ami-0f58b397bc5c1f2e8"
}