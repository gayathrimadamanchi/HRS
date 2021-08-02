resource "docker_container" "wordpress" {
   count = var.wordpress_instance_count 
   name  = "wordpress_instance_${count.index}"
   image = "wordpress:latest"
   restart = "always"

   ports {
   	internal = "80"
    	external = var.external_port[count.index]
  }
}