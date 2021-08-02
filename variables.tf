variable "wordpress_instance_count" {
  type = number
  default = 3
}
variable "external_port"{
  type = map
  default = {
    "0" = "9110"
    "1" = "9120"
    "2" = "9130"
  }
}