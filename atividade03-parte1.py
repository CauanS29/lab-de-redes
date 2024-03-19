#!/usr/bin/python

import subprocess


def start_capture(output_file):
    command = f"sudo tshark -w {output_file}"
    capture_process = subprocess.Popen(command, shell=True)
    return capture_process

def stop_capture(process):
    process.terminate()

def get_ip_port(service_name):
    command = f"nslookup {service_name} | grep 'Address:'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    if len(lines) >= 2:
        ip = lines[1].split(':')[1].strip()
        return ip
    else:
        return None

def check_service(ip, port):
    command = f"nc -zv {ip} {port}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return "succeeded" in result.stdout.lower()

def main():
    dns_ip = get_ip_port("example.com")
    web_ip = get_ip_port("example.com")

    output_file = "traffic_capture.pcap"
    capture_process = start_capture(output_file)

    host = "example.com"
    response = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE)
    if response.returncode == 0:
        print(f"Host {host} esta online.")
    else:
        print(f"Host {host} esta offline.")

    if dns_ip and check_service(dns_ip, 53):
        print("Servico de Nome esta respondendo corretamente.")
    else:
        print("Falha ao testar o Servico de Nome.")

    if web_ip and check_service(web_ip, 80):
        print("Servico Web esta respondendo corretamente.")
    else:
        print("Falha ao testar o Servico Web.")

    input("Pressione Enter para terminar a captura de trafego...")
    stop_capture(capture_process)
    print("Captura de trafego terminada.")

if __name__ == "__main__":
    main()
