#!/bin/bash

printf "Iniciando descarga IDV_5.7...\n"

if [ -d ~/Downloads/ ]
then wget https://www.unidata.ucar.edu/downloads/idv/current/ftp/idv_5_7_linux64_installer.sh -P ~/Downloads/
	printf "\nDescarga Finalizada \n  \n---------------------- \n  \nInstalando IDV_5.7...\n"
	if bash ~/Downloads/idv_5_7_linux64_installer.sh -q
	then
		printf "\nInstalación Finalizada \n  \n---------------------- \n  \nInstalando librerías de Python-3...\n"
		if sudo apt install python3-tk && sudo apt-get install python3-pil python3-pil.image
		then 	
			printf "\nInstalación de Tkinter y PIL Finalizada \n  \n---------------------- \n  \nDescomprimiendo el programa VIS...\n"
			if tar -Jxvf VIS.tar.xz -C ~/Desktop/
			then
              			printf "\nProceso terminado con éxito!!\n  \n---------------------- \n  \nModificando los archivos .isl...\n"
				if find ~/Desktop/VIS/Paises/ -name *.isl -exec sed -i -e 's/anthony\/Escritorio/'"$USER"'\/Desktop/g' {} \; && find ~/Desktop/VIS/Codigo/ -name VIS.py -exec sed -i -e 's/Escritorio/Desktop/g' {} \; && find ~/Desktop/ -name VIS.desktop -exec sed -i -e 's/anthony\/Escritorio/'"$USER"'\/Desktop/g' {} \;
				then
					printf "\nModificado con éxito!\n"
					printf "Creado por el Lic. Anthony Segura Garcia en colaboracion entre la Universidad de Costa Rica y el Instituto Meteorologico Nacional."
				else
					printf "\nError: No se pudieron modificar los archivos\n"
				fi
			else 
				printf "\nError: No se pudo completar el proceso\n"
			fi
		else
			printf "\nError: No se pudieron instalar las librerías de Python3 necesarias\n"
		fi
	else
		printf "\nError: No se pudo instalar el programa\n"
	fi
else
        printf "\nError: No se pudo descargar el archivo\n"
	if [ -d ~/Descargas/ ]
	then wget https://www.unidata.ucar.edu/downloads/idv/current/ftp/idv_5_7_linux64_installer.sh -P ~/Descargas/
		printf "\nDescarga Finalizada \n  \n---------------------- \n  \nInstalando IDV_5.7...\n"
		if bash ~/Descargas/idv_5_7_linux64_installer.sh -q
	   	then
			printf "\nInstalación Finalizada \n  \n---------------------- \n  \nInstalando librerías de Python-3...\n"
			if sudo apt install python3-tk && sudo apt-get install python3-pil python3-pil.image
			then
				printf "\nInstalación de Tkinter y PIL Finalizada \n  \n---------------------- \n  \nDescomprimiendo el programa VIS...\n"
				if tar -Jxvf VIS.tar.xz -C ~/Escritorio/
				then
					printf "\nProceso terminado con éxito!!\n  \n---------------------- \n  \nModificando los archivos .isl...\n"
					if find ~/Escritorio/VIS/Paises/ -name *.isl -exec sed -i -e 's/anthony\/Desktop/'"$USER"'\/Escritorio/g' {} \; && find ~/Escritorio/VIS/Codigo/ -name VIS.py -exec sed -i -e 's/Desktop/Escritorio/g' {} \;  && find ~/Escritorio/ -name VIS.desktop -exec sed -i -e 's/anthony\/Desktop/'"$USER"'\/Escritorio/g' {} \;
					then
						printf "\nModificado con éxito!\n"
						printf "Creado por el Lic. Anthony Segura Garcia en colaboracion entre la Universidad de Costa Rica y el Instituto Meteorologico Nacional."
					else
						printf "\nError: No se pudieron modificar los archivos\n"
					fi
				else
					printf "\nError: No se pudo completar el proceso\n"
				fi
			else
				printf "\nError: No se pudieron instalar las librerías de Python3 necesarias\n"
			fi
		else                    
			printf "\nError: No se pudo instalar el programa\n"
		fi
	else
		printf "\nError: No se pudo descargar el archivo\n"
	fi
fi
