import sys
import threading
from subprocess import Popen, PIPE


python_version = sys.version_info.major

if python_version == 2:
	input = raw_input

class ThreadCheckIp(threading.Thread):
	def __init__(self, _ip):
		threading.Thread.__init__(self)
		self.ip = _ip

	def run(self):
		direccion_ip = self.ip
		process = Popen(['/bin/ping','-c 1 -W 100', direccion_ip],stdout=PIPE,stdin=PIPE,stderr=PIPE)
		stdout, stderr = process.communicate(input=None)
		
		if "bytes from" in stdout:
			print("IP {0} esta siendo usada".format(direccion_ip))
		else:
			print("IP {0} esta disponible".format(direccion_ip))


def check_ip_thread():

	print("Escriba una X donde quiere hacer la busqueda")
	
	formato_ip = input("Escriba el formato de la ip Ej 192.168.1.x -> ")
	rango_min = int(input("Escriba el rango minimo de la busqueda [0-255] ->"))
	rango_max = int(input("Escriba el rango maximo de la busqueda [0-255] ->"))

	if rango_min > 255 and rango_min < 0:
		print("Error el rango minimo seleccionado es incorrecto")

	if rango_max > 255 and rango_max < 0:
		print("Error el rango maximo seleccionado es incorrecto")


	for num in range(rango_min, rango_max):
		
		tmp_ip = formato_ip.replace("x", "{0}").format(num)
		
		hilo = ThreadCheckIp(tmp_ip)

		hilo.start()



check_ip_thread()