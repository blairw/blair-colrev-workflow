import bibtexparser
import pandas as pd

OUTPUT_DIR = "00-outputs"
INCLUDES1_STATUS_LIST = [
	"rev_prescreen_included"
]
INCLUDES2_STATUS_LIST = [
	"rev_synthesized"
]
EXCLUDES_STATUS_LIST = [
	"rev_excluded",
	"rev_prescreen_excluded"
]
PENDING_STATUS_LIST = [
	"md_imported"
]

# LOAD COLREV PARTS

dict_bibdata = {}
with open('../data/records.bib') as bibtex_file:
	bibdb = bibtexparser.load(bibtex_file)
	dict_bibdata = bibdb.entries

df_bibdb = pd.DataFrame(dict_bibdata)
df_bibdb = df_bibdb.replace(r'\n', ' ', regex=True)

df_subsetcolumns = df_bibdb[["ID", "year", "doi", "title", "colrev_status", "screening_criteria", "author", "journal", "abstract", "keywords", "colrev_origin"]]
df_subsetcolumns = df_subsetcolumns.rename(columns={"ID": "paper_id"})
df_subsetcolumns = df_subsetcolumns.rename(columns={"year": "year_published"})

df_ALLRECORDS = df_subsetcolumns.sort_values(by="paper_id", key=lambda col: col.str.lower()) # Adapted from https://stackoverflow.com/a/63141564
df_INCLUDED1 = df_ALLRECORDS.loc[df_ALLRECORDS["colrev_status"].isin(INCLUDES1_STATUS_LIST)]
df_INCLUDED2 = df_ALLRECORDS.loc[df_ALLRECORDS["colrev_status"].isin(INCLUDES2_STATUS_LIST)]
df_EXCLUDED = df_ALLRECORDS.loc[df_ALLRECORDS["colrev_status"].isin(EXCLUDES_STATUS_LIST)]
df_PENDING = df_ALLRECORDS.loc[df_ALLRECORDS["colrev_status"].isin(PENDING_STATUS_LIST)]

df_ALLRECORDS.to_csv(OUTPUT_DIR + "/df_ALLRECORDS.csv", index=False)
df_ALLRECORDS.to_html(OUTPUT_DIR + "/df_ALLRECORDS.html", index=False)
df_INCLUDED1.to_csv(OUTPUT_DIR + "/df_INCLUDED1.csv", index=False)
df_INCLUDED1.to_html(OUTPUT_DIR + "/df_INCLUDED1.html", index=False)
df_INCLUDED2.to_csv(OUTPUT_DIR + "/df_INCLUDED2.csv", index=False)
df_INCLUDED2.to_html(OUTPUT_DIR + "/df_INCLUDED2.html", index=False)
df_EXCLUDED.to_csv(OUTPUT_DIR + "/df_EXCLUDED.csv", index=False)
df_EXCLUDED.to_html(OUTPUT_DIR + "/df_EXCLUDED.html", index=False)
df_PENDING.to_csv(OUTPUT_DIR + "/df_PENDING.csv", index=False)
df_PENDING.to_html(OUTPUT_DIR + "/df_PENDING.html", index=False)

print("Done!")
