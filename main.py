# -*- coding: utf-8 -*-
import netifaces
import os
import subprocess

#ping 测试
# ping通返回 TRUE，否则为F
def pingtest(gateway):
	fnull = open(os.devnull, 'w')
	result = not subprocess.call('ping '+gateway, shell = True, stdout = fnull, stderr = fnull)
	if result:
		print("ping ok")
	else:
		print ("ping fail")
	fnull.close()
	return result

def main():
	gws= netifaces.gateways()
	#print(gws)
	dgw=gws['default'][netifaces.AF_INET][0]
	#print(dgw)
	results = []
	for i in netifaces.interfaces():
		info = netifaces.ifaddresses(i)
		#print(info[netifaces.AF_INET][0]['addr'])
		print(info)
		if netifaces.AF_INET not in info:
			continue
		results.append(info[netifaces.AF_INET][0]['addr'])
	print(results)
	result= pingtest(dgw)
	print(type(dgw))
	#if sdgw==u'19' and  pingts:
		#print(sdgw)
		#os.system("route add 19.0.0.0 mask 255.0.0.0 " +dgw)

if __name__ == '__main__':
	main()