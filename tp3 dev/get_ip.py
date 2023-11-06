from psutil import net_if_addrs

def get_wireless_ip(wireless_interface_name):
    # Itération sur les interfaces réseau disponibles
    for interface in net_if_addrs():
        # Recherche de l'interface sans fil spécifiée
        if interface == wireless_interface_name:
            # Itération sur les adresses associées à l'interface sans fil
            for address in net_if_addrs()[interface]:
                # Vérification de la famille d'adresse (IPv4 a une famille de 2)
                if address.family == 2:
                    # Retourne l'adresse IP IPv4 trouvée
                    return address.address

    return None

wireless_interface_name = 'Wi-Fi'

def ip():
    if __name__ == "__main__":
    # Appelle la fonction get_wireless_ip() en spécifiant le nom de l'interface sans fil
        ip = get_wireless_ip(wireless_interface_name)
        if ip:
            print(f"Adresse IP de l'interface {wireless_interface_name}: {ip}")
        else:
            print(f"Aucune adresse IP IPv4 trouvée pour l'interface {wireless_interface_name}.")