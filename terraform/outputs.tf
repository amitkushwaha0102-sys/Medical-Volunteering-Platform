output "ec2_public_ip" {
  description = "public ip require for output"
  value       = aws_instance.application_server_ec2.public_ip
}

output "rds_endpoint" {
  description = "public ip require for output"
  value       = aws_db_instance.db_server_ec2.endpoint
}

output "vpc_id" {
  description = "vpc require for id"
  value       = aws_vpc.main.id
}

output "alb_dns_name" {
  description = "ALB DNS name to access application"
  value       = aws_lb.main.dns_name
}