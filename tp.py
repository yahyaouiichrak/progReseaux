from netmiko import ConnectHandler 

routeur = {
	'device_type':'cisco_ios',
	'host':'sandbox-iosxe-latest-1.cisco.com',
	'username':'admin',
	'password':'C1sco12345',
	'port':22,
}

try: 
	connection = ConnectHandler(**routeur)
	print("Connexion réussi ")
	print("affichage de l'heure :")
	output_clock = connection.send_command("show clock")
	print(output_clock)
	print("enregistrement des interfaces dans 'interfaces.txt'...")
	output_interfaces = connection.send_command("show ip interface brief")
	with open("interfaces.txt", "w") as file:
		file.write(output_interfaces)
	
	print("Configuration de l'interface loopback")
	config_commands = [
		"interface loopback0",
		"ip address 10.8.8.8 255.255.255.240",
		"no shutdown"
	]

	connection.send_config_set(config_commands)
	print("interface loopback configurée avec succées")
	connection.disconnect()
	print("déconnecté du r")
except Exception as e:
	print(f"erreur: {e}")
