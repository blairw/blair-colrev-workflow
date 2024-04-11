python ./records_to_csv.py

for this_file in "df_ALLRECORDS" "df_EXCLUDED" "df_INCLUDED1" "df_INCLUDED2" "df_PENDING"
do
	cat "00-fragments/0100-top.html" > "00-outputs/${this_file}_formatted.html"
	cat "00-outputs/${this_file}.html" >> "00-outputs/${this_file}_formatted.html"
	cat "00-fragments/0900-bottom.html" >> "00-outputs/${this_file}_formatted.html"
done
