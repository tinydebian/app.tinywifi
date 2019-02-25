################################################################################
# Enable auto login as root via ttyS0 (UART)

cp serial-getty@ttyS0.service /etc/systemd/system/
systemctl enable serial-getty\@ttyS0.service

