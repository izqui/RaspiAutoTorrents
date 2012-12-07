Adding torrents automatically to Raspberry Pi
=================================================

[Blog post] (http://izqui.me/post/37407490216/automatically-adding-torrents-to-raspberry-pi)

First of all you need to install the python module that will talk to transmission-rpc:
    
     pip install transmissionrpc
     
Now edit the scripts with your raspi IP, transmission user and passwd.

###Transmission configuration

You need to install trasnmission-daemon in your Raspi

    sudo apt-get install transmission-daemon
    
You now need to change the settings:

Stop the server

    sudo /etc/init.d/transmission-daemon stop
    
Edit settings

    sudo nano /etc/transmission-daemon/settings.json
  
Edit this
    
    "rpc-password": "your pass",
    "rpc-username": "your username",
    "rpc-whitelist": "*.*.*.*"

Save and start again

    sudo /etc/init.d/transmission-daemon start

###addt configuration

Move the script to '/usr/bin' and make it executable:
    cd /usr/bin
    sudo chmod 755 addt
    
Now you can type 'addt' and add links

###Torrents auto adding

Create '~/Torrents' and save the folder action script included. Place torrents.py in your Torrents directory and you are good to go.

To test it save a torrent in this dir and you will see it added in your Raspi.


Feel free to contribute! 

     
