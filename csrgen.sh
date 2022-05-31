#!/bin/bash

clear

echo "Voor wie?"
echo "1) Intern"
echo "2) Klanten"
read -r org


echo "Common name: "
read -r cn
output_dir=/home/ssl

function generate_certificate(){
	EC_TMPFILE=$(mktemp)
	openssl genpkey -genparam -algorithm ec -pkeyopt ec_paramgen_curve:secp384r1 > $EC_TMPFILE
	mkdir -p "$output_dir/$org/"
	openssl_cmd="openssl req -nodes -newkey ec:$EC_TMPFILE -keyout $output_dir/$org/$cn.key -out $output_dir/$org/$cn.csr"
	$openssl_cmd
	cat "$output_dir/$org/$cn.csr"
}
if [ "$org" == 1 ];
then
	org=intern
	generate_certificate
else
	org=klanten
	generate_certificate
fi
