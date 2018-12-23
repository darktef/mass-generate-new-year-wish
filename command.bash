magick -list font # to find the folder where magick place the font
find /Users/darktef/Library/Fonts -type f -name '*.*' | perl imagick_type_gen -f - > type.xml # find all customized font and port into type.xml
# go to the magick font folder and include that newly generated type.xml to the original type.xml
convert -background transparent -fill black -pointsize 72 label:hello label.gif
convert -font NotoSansMonoCJKtc -pointsize 72 -background transparent label:"张" label.gif
convert -font NotoSansMonoCJKtc -pointsize 72 -background transparent label:"张" label.gif
convert happy_new_year.jpg -font NotoSansMonoCJKtc -pointsize 48 -annotate +50+50 “祝您新年快乐” result.jpg
convert happy_new_year.jpg -font NotoSansMonoCJKtc -fill "#D21F3C" -pointsize 128 -annotate +310+400 祝您新年快乐! result.jpg
