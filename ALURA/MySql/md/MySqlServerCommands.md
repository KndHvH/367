# MySqlServer

#### 1.Install

##### Update:

    sudo apt update
    sudo apt list --upgradable # get a list of upgrades
    sudo apt upgrade

##### Install:

    apt install mysql-server-8.0

#### 2.Setup

    sudo mysql
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'My7Pass@Word_9_8A_zE';
    exit


#### 3.Status

    sudo systemctl start mysql.service
    sudo systemctl stop mysql.service
    sudo systemctl restart mysql.service
    sudo systemctl status mysql.service


#### 4.Secure
    sudo mysql_secure_installation


#### 5.Boot
    sudo systemctl is-enabled mysql.service
    else:  sudo systemctl enable mysql.service
    sudo systemctl status mysql.service


#### 6.Login
    mysql -u {user} -p
    mysql -u {user} -h {remote_server_ip} -p
    mysql -u root -p