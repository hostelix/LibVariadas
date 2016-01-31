from subprocess import Popen, PIPE

def ips_disponibles(rango_min=1, rango_max=254, formato_ip="192.168.1.%d"):
	for n in range(int(rango_min), int(rango_max)):
		direccion_ip = str(formato_ip)%n
		process = Popen(['/bin/ping','-c 1', direccion_ip],stdout=PIPE,stdin=PIPE,stderr=PIPE)
		stdout, stderr = process.communicate(input=None)
		
		if "bytes from " in stdout:
			print "IP %s esta siendo usada"%(direccion_ip)

