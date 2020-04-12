## EyeDoc
EyeDoc will forward dockersocket events with data about freshly deployed containers and their network coordinates.

### Install
    $> git clone https://github.com/psytron/eyedoc.git && cd eyedoc && ./install.py <web_proxy_address>
The install script will simply copy the SystemD init file into /etc/systemd. 
