#!/bin/bash
# Program:
#        Install Supermicro Thin-agent
# History:
# 20140123 billw
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH
prog="Thin-Agent Service"
directory="/opt/supermicro"
typeset ret_code
ret=""
os="other"
# echo "os="$os
force=$1

if grep "debian" /etc/os-release -i -q; then
	os="debian"
  # echo $os
fi

if grep "ubuntu" /etc/os-release -i -q; then
	os="ubuntu"
  # echo $os
fi

if grep "suse" /etc/os-release -i -q; then
	os="suse"
  # echo $os
fi

os_ver=$(grep 'VERSION_ID' /etc/os-release | cut -d '"' -f 2 | cut -d '.' -f 1)

ipmi_msghandler_missing() {
  echo "Module ipmi_msghandler not found."
}

ipmi_devintf_missing() {
  echo "Module ipmi_devintf not found."
}

ipmi_si_missing() {
  echo "Module ipmi_si not found."
}

ethtoolFail() {
  echo "install ethtool....."
  if [ "$os" == "other" ]; then
    yum install ethtool -y
    ret=$(rpm -q ethtool)
    ret_code=$?
  elif [ "$os" == "suse" ]; then
    zypper install -y ethtool
    ret=$(rpm -q ethtool)
    ret_code=$?
  else
    apt-get install ethtool -y
    ret=$(dpkg-query -W ethtool)
    ret_code=$?
 fi
 [ $ret_code == 0 ] || fail
}

mdadmFail() {
  #echo "install mdadm....."
  while true; do
    if [ "$force" == "-y" ]; then
		  yn="Y"
	  else
		  read -p "To enable Intel RSTe information, please install mdadm package [y/n] " yn
	  fi

	  case $yn in
      [Yy]* )    
			  if [ "$os" == "other" ]; then
				  yum install mdadm -y
				  ret=$(rpm -q mdadm)
				  ret_code=$?
        elif [ "$os" == "suse" ]; then
				  zypper install -y mdadm
    		  ret=$(rpm -q mdadm)
				  ret_code=$?
			  else
				  apt-get install mdadm -y
		  		ret=$(dpkg-query -W mdadm)
			  	ret_code=$?
			  fi
        [ $ret_code == 0 ] || fail
        break;;
      [Nn]* ) break;;
      * ) echo "Please answer yes or no.";
    esac
  done
}

routeFail() {
  echo "install net-tools....."
  if [ "$os" == "other" ]; then
    yum install net-tools -y
    ret=$(rpm -q net-tools)
    ret_code=$?
  elif [ "$os" == "suse" ]; then
    zypper install -y net-tools
    ret=$(rpm -q net-tools)
    ret_code=$?
  else
    apt-get install net-tools -y
    ret=$(dpkg-query -W net-tools)
    ret_code=$?
  fi
  [ $ret_code == 0 ] || fail
}

lsscsiFail() {
  echo "install lsscsi....."
  if [ "$os" == "other" ]; then
    yum install lsscsi -y
    ret=$(rpm -q lsscsi)
    ret_code=$?
  elif [ "$os" == "suse" ]; then
    zypper install -y lsscsi
    ret=$(rpm -q lsscsi)
    ret_code=$?
  else
    apt-get install lsscsi -y
    ret=$(dpkg-query -W lsscsi)
    ret_code=$?
  fi
  [ $ret_code == 0 ] || fail
}

bcFail() {
  echo "install bc....."
  if [ "$os" == "other" ]; then
    yum install bc -y
    ret=$(rpm -q bc)
    ret_code=$?
  elif [ "$os" == "suse" ]; then
    zypper install -y bc
    ret=$(rpm -q bc)
    ret_code=$?
  else
    apt-get install bc -y
    ret=$(dpkg-query -W bc)
    ret_code=$?
  fi
  [ $ret_code == 0 ] || fail

}

lspciFail() {
  echo "install pciutils....."
  if [ "$os" == "other" ]; then
    yum install pciutils -y
    ret=$(rpm -q pciutils)
    ret_code=$?
  elif [ "$os" == "suse" ]; then
    zypper install -y pciutils
    ret=$(rpm -q pciutils)
    ret_code=$?
  else
    apt-get install pciutils -y
    ret=$(dpkg-query -W pciutils)
    ret_code=$?
  fi
  [ $ret_code == 0 ] || fail
}

smarttoolFail() {
  #echo "install smartmontools....."
  while true; do
    if [ "$force" == "-y" ]; then
		  yn="Y"
	 else
		  read -p "To enable SMART HDD information, please install smartmontools package [y/n] " yn
	 fi

	 case $yn in
     	[Yy]* )    
  			if [ "$os" == "other" ]; then
  				yum install smartmontools* -y
  				ret=$(rpm -q smartmontools)
  				ret_code=$?
  			elif [ "$os" == "suse" ]; then
  				zypper install -y smartmontools*
  				ret=$(rpm -q smartmontools)
  				ret_code=$?
  			else
  				apt-get install smartmontools* -y
  				ret=$(dpkg-query -W smartmontools)
  				ret_code=$?
  			fi
  			[ $ret_code == 0 ] || fail
        break;;
      [Nn]* ) break;;
      * ) echo "Please answer yes or no.";
    esac
  done
}

fail() {
  echo "install fail"
  exit 1
}

IPMITAS_missing() {
  echo "IPMITAS not found"
  fail
}

tas_missing() {
  echo "tas not found"
  fail
}

watchtas_missing() {
  echo "watchtas not found"
  fail
}

storcli_missing() {
  echo "storcli not found"
  fail
}

sas3ircu_missing() {
  echo "sas3ircu not found"
  fail
}

copyFile() {
  cp -rf IPMITAS "$directory"
  #2023/03/22 update
  if [ -d "/etc/init.d/" ]
  then
    cp -rf tas /etc/init.d/
  else
    mkdir /etc/init.d/
    cp -rf tas /etc/init.d/
  fi
  cp -rf watchtas "$directory"
  cp -rf storcli /usr/bin
  cp -rf sas3ircu /usr/bin
  cp -rf license.txt "$directory"

  [ -d /usr/local/lib/systemd ] || mkdir /usr/local/lib/systemd
  [ -d /usr/local/lib/systemd/system ] || mkdir /usr/local/lib/systemd/system
  cp -rf tas.service /usr/local/lib/systemd/system 2> /dev/null
  systemctl enable tas
  systemctl daemon-reload

  # echo ""
  # echo "*****StorCLI License start*****"
  # cat $directory/license.txt
  # echo "*****StorCLI License end*****"
}

checkIPMI() {
  ret_code=1
  if [ "$os" == "other" ];then
      ret=$(service ipmi status | grep ipmi_msghandler)
      ret_code=$?
      echo "Install OpenBMC if ipmi.service could not be found."
      # yum install OpenBMC -y
  fi
  if [ $ret_code == 1 ]; then
      ret=$(modprobe ipmi_msghandler)
      ret_code=$?
      [ $ret_code == 0 ] || ipmi_msghandler_missing
  fi

  ret_code=1
  if [ "$os" == "other" ];then
      ret=$(service ipmi status | grep ipmi_devintf)
      ret_code=$?
  fi
  if [ $ret_code == 1 ]; then
  	ret=$(modprobe ipmi_devintf)
    ret_code=$?
    [ $ret_code == 0 ] || ipmi_devintf_missing
  fi

  ret_code=1
  if [ "$os" == "other" ];then
      ret=$(service ipmi status | grep ipmi_si)
      ret_code=$?
  fi
  if [ $ret_code == 1 ]; then
  	ret=$(modprobe ipmi_si)
  	ret_code=$?
  	[ $ret_code == 0 ] || ipmi_si_missing
  fi
}

checkTool() {
  if [ "$os" == "other" ] || [ "$os" == "suse" ]; then
    ret=$(rpm -q ethtool)
    echo $ret 
    ret_code=$?
    [ $ret_code == 0 ] || ethtoolFail
    ret=$(rpm -q smartmontools)
    echo $ret
    ret_code=$?
    [ $ret_code == 0 ] || smarttoolFail
    ret=$(rpm -q mdadm)
    echo $ret
    ret_code=$?
    [ $ret_code == 0 ] || mdadmFail
    ret=$(rpm -q net-tools)
    echo $ret
    ret_code=$?
    [ $ret_code == 0 ] || routeFail
    ret=$(rpm -q lsscsi)
    echo $ret
    ret_code=$?
    [ $ret_code == 0 ] || lsscsiFail
    ret=$(rpm -q bc)
    echo $ret
    ret_code=$?
    [ $ret_code == 0 ] || bcFail
    ret=$(rpm -q pciutils)
    echo $ret
    ret_code=$?
    [ $ret_code == 0 ] || lspciFail	
  else
    ret=$(dpkg-query -l ethtool | grep ethtool | awk '{print $1}')
    ret_code=$?
    [ $ret_code == 0 ] || ethtoolFail
    [ "$ret" == "ii" ] || ethtoolFail
    ret=$(dpkg-query -l smartmontools | grep smartmontools | awk '{print $1}')
    ret_code=$?
    [ $ret_code == 0 ] || smarttoolFail
    [ "$ret" == "ii" ] || smarttoolFail
    ret=$(dpkg-query -l mdadm | grep mdadm | awk '{print $1}')
    ret_code=$?
    [ $ret_code == 0 ] || mdadmFail
    [ "$ret" == "ii" ] || mdadmFail
    ret=$(dpkg-query -l net-tools | grep net-tools | awk '{print $1}')
    ret_code=$?
    [ $ret_code == 0 ] || routeFail
    [ "$ret" == "ii" ] || routeFail
    ret=$(dpkg-query -l lsscsi | grep lsscsi | awk '{print $1}')
    ret_code=$?
    [ $ret_code == 0 ] || lsscsiFail
    [ "$ret" == "ii" ] || lsscsiFail	
    ret=$(dpkg-query -l bc | grep bc | awk '{print $1}')
    ret_code=$?
    [ $ret_code == 0 ] || bcFail
    [ "$ret" == "ii" ] || bcFail
    ret=$(dpkg-query -l pciutils | grep bc | awk '{print $1}')
    ret_code=$?
    [ $ret_code == 0 ] || lspciFail
    [ "$ret" == "ii" ] || lspciFail
  fi

  if [[ "$os" == "suse" && "$os_ver" -ge 15 ]]; then
    if ! rpm -q insserv-compat > /dev/null; then
      echo "install insserv-compat....."
      if ! zypper install -y insserv-compat > /dev/null; then
        fail
      fi
    fi
  fi
}
#3/23 Create AddPermission()
AddPermission(){
  chmod +x *
}

check() {
  #3/23 Update else behavior
  [ -f IPMITAS ] || IPMITAS_missing
  [ -f tas ] || tas_missing
  [ -f watchtas ] || watchtas_missing
  [ -f storcli ] || storcli_missing
  [ -f sas3ircu ] || sas3ircu_missing

  if [ -x IPMITAS ]; then
    if [ -x tas ]; then
      if [ -x watchtas ]; then
        # echo "Run - CheckTool()"
        checkTool
        # echo "Run - CheckIPMI()"
        checkIPMI
      else
        echo "watchtas not executable"
        echo "Adding execute permission"
        AddPermission
        echo "Permission added, please re-run the script"
        fail
      fi   
    else
      echo "tas not executable"
      echo "Adding execute permission"
      AddPermission
      echo "Permission added, please re-run the script"
      fail
    fi       
  else
    echo "IPMITAS not executable"
    echo "Adding execute permission"
    AddPermission
    echo "Permission added, please re-run the script"
    fail
  fi
}

startup() {
  # echo "os=" $os #other
  # echo "os ver=" $os_ver #9
  if [[ "$os" == "suse" && "$os_ver" -ge 15 ]]; then
	:
  elif [ "$os" == "suse" ]; then
    ln -f -s /etc/init.d/tas /etc/init.d/rc0.d/S99tas
    ln -f -s /etc/init.d/tas /etc/init.d/rc1.d/S99tas
    ln -f -s /etc/init.d/tas /etc/init.d/rc2.d/S99tas
    ln -f -s /etc/init.d/tas /etc/init.d/rc3.d/S99tas
    ln -f -s /etc/init.d/tas /etc/init.d/rc4.d/S99tas
    ln -f -s /etc/init.d/tas /etc/init.d/rc5.d/S99tas
    ln -f -s /etc/init.d/tas /etc/init.d/rc6.d/S99tas
  else
    # Update on 3/22
    if [ -d "/etc/rc0.d/" ]; then
      ln -f -s /etc/init.d/tas /etc/rc0.d/S99tas
    else
      mkdir /etc/rc0.d
      ln -f -s /etc/init.d/tas /etc/rc0.d/S99tas
    fi
    if [ -d "/etc/rc1.d/" ]; then
      ln -f -s /etc/init.d/tas /etc/rc1.d/S99tas
    else
      mkdir /etc/rc1.d/
      ln -f -s /etc/init.d/tas /etc/rc1.d/S99tas
    fi
    if [ -d "/etc/rc2.d/" ]; then
      ln -f -s /etc/init.d/tas /etc/rc2.d/S99tas
    else
      mkdir /etc/rc2.d/
      ln -f -s /etc/init.d/tas /etc/rc2.d/S99tas
    fi
    if [ -d "/etc/rc3.d/" ]; then
      ln -f -s /etc/init.d/tas /etc/rc3.d/S99tas
    else
      mkdir /etc/rc3.d/
      ln -f -s /etc/init.d/tas /etc/rc3.d/S99tas
    fi
    if [ -d "/etc/rc4.d/" ]; then
      ln -f -s /etc/init.d/tas /etc/rc4.d/S99tas
    else
      mkdir /etc/rc4.d/
      ln -f -s /etc/init.d/tas /etc/rc4.d/S99tas
    fi
    if [ -d "/etc/rc5.d/" ]; then
      ln -f -s /etc/init.d/tas /etc/rc5.d/S99tas
    else
      mkdir /etc/rc5.d/
      ln -f -s /etc/init.d/tas /etc/rc5.d/S99tas
    fi
    if [ -d "/etc/rc6.d/" ]; then
      ln -f -s /etc/init.d/tas /etc/rc6.d/S99tas
    else
      mkdir /etc/rc6.d/
      ln -f -s /etc/init.d/tas /etc/rc6.d/S99tas
    fi
  fi

  if [[ "$os" == "suse" && "$os_ver" -ge 15 ]]; then
	:
  elif [ "$os" == "other" ] || [ "$os" == "suse" ]; then
    chkconfig tas on
  else
    update-rc.d -f tas remove
    update-rc.d tas defaults
  fi
}

echo "Install" $prog
# echo "Run check()"
check 
# echo "Check() completed"

if [ -d "$directory" ]
then
#  echo "Run copyFile"
 copyFile 
#  echo "copyFile() completed"
else
  echo "No" $directory
  mkdir "$directory"
  copyFile
fi

# echo "Run startup()"
startup 
echo "Install success..."

killall IPMITAS 2> /dev/null
if [ $? != 0 ]; then
  pkill -9 -x IPMITAS
fi

killall watchtas 2> /dev/null
if [ $? != 0 ]; then
  pkill -9 -x watchtas
fi

if ! command -v systemctl &> /dev/null
then
  /etc/init.d/tas start
else
  systemctl restart tas
fi
