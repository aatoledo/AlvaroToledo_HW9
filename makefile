cpp_vs_python.png: times_python.csv times_cpp.csv 
	python AlvaroToledo_Graficas.py

times_cpp.csv: gen_times.x
	./gen_times.x > times_cpp.csv

times_python.csv:
	python AlvaroToledo_GenerarTiempos.py > times_python.csv

gen_times.x:
	g++ AlvaroToledo_GenerarTiempos.cpp -o gen_times.x

clean:
	rm *.csv
	rm *.x
	rm *.png
