# display_ip_address
Script to display ip address on raspberry pi screen on startup

Open the Autostart File for Editing:

Open the LXDE-pi autostart file in a text editor:

```nano ~/.config/lxsession/LXDE-pi/autostart```


Adjust the Contents of the Autostart File:
The autostart file should include the command to start the LXDE environment as well as your script. The default content usually includes several lines that start with @ symbol. Your file should look something like this:

```
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash
@point-rpi
@python3 {path to this folder}/display_ip_address/ipaddress.py
```


Make sure that the lines for lxpanel, pcmanfm, and other LXDE components are present. Then, add your script at the end of the file.

Save and Close the File:

Save the file and exit the editor (Ctrl + X, then Y, and Enter if you're using nano).

Reboot Your Raspberry Pi:

Reboot your Raspberry Pi to see if the issue is resolved:

```
sudo reboot
```
