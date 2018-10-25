filename=domain_adaptation
pdf: ${filename}.tex
	pdflatex ${filename} && biber ${filename} && pdflatex ${filename}
clean: 
	rm -f ${filename}.{ps,pdf,log,aux,out,dvi,bbl,blg}
