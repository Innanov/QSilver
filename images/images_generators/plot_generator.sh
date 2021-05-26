for file in *.tex; do
	pdflatex $file
done

rm *.aux *.log *.synctex.gz *.fls

for file in *.pdf; do
	echo "$(echo $file | cut --delimiter="." --fields=1)"
	convert -density 300 $file -quality 100 -colorspace RGB "../$(echo $file | cut --delimiter='.' --fields=1).png"
done
