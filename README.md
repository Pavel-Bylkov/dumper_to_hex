# dumper_to_hex
Util in Python - get Hex dump for any file or get file from hex dump
Help for Dumper to HEX

	-d --dump Default action - create txt file with HEX code
	-l --load Read txt file with HEX code and create 
	-s --src Source file or path
	-o --out Output file or path

Example: 
python dumper_to_hex.py app.exe
result - app.exe.txt
python dumper_to_hex.py -d -s app.exe
result - app.exe.txt
python dumper_to_hex.py -d -s app.exe -o out.txt
result - out.txt
python dumper_to_hex.py -l -s app.exe.txt -o out.exe
result - out.exe
python dumper_to_hex.py -l -s app.exe.txt
result - app.exe
