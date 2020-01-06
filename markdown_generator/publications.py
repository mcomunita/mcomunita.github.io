
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
# 

# ## Data format
# 
# The TSV needs to have the following columns: date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top.
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. 
# - `date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

# In[2]:

import pandas as pd


# ## Import TSV
# 
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:

#publications = pd.read_csv("publications.tsv", sep="\t", header=0, encoding='latin-1')
publications = pd.read_excel("publications.xlsx", sep="\t", header=0, encoding='latin-1')


# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

# In[4]:

html_escape_table = {
    '"': "&quot;",
    "'": "&apos;",
    }

def html_escape(text):
    """Produce entities within text."""
    temp = text.encode('ascii', 'xmlcharrefreplace').decode('utf8')
    return "".join(html_escape_table.get(c, c) for c in temp)


# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

# In[5]:
overwrite = False
base_file_path = '/files'
base_image_path = '/assets/images'
publications_dir = '/_publications'

cat_dict = {'sed':'Sound Event Detection',
            'mir': 'Music Information Retrieval',
            'iap': 'Natural Audio Production Interfaces',
            'crowd': 'Crowdsourced Audio Annotation and Quality Evaluation',
            'rep': 'Representation Learning',
            'nime': 'New Interfaces for Musical Expression'}

import os
for row, item in publications.iterrows():

    url_slug = os.path.splitext(item.paper_url)[0]
    paper_url = os.path.join(base_file_path, item.paper_url)

    date = item.date.strftime('%Y-%m-%d')
    md_filename = str(date) + "-" + url_slug + ".md"
    if os.path.exists(os.path.join(publications_dir, md_filename)):
        continue

    html_filename = str(date) + "-" + url_slug
    year = date[:4]
    
    ## YAML variables
    md = "---\nlayout: default-publication"

    md += "\ntitle: \""   + item.title + '"\n'
    
    md += """collection: publications"""
    
    md += """\npermalink: /publications/""" + html_filename
    
    if len(str(item.abstract)) > 5:
        md += '\nabstract: "' + html_escape(item.abstract) + '"'
    
    md += "\ndate: " + str(date)
    
    md += "\nvenue: '" + html_escape(item.venue) + "'"
    
    if len(str(item.paper_url)) > 5:
        md += "\npaperurl: '" + paper_url + "'"

    if len(str(item.image_url)) > 5:
        md += "\nimage: '" + os.path.join(base_image_path, item.image_url) + "'"

    if len(str(item.image_align)) > 3:
        md += "\nimagealign: " + str(item.image_align)

    if len(str(item.image_width)) > 3:
        md += "\nimagewidth: " + str(item.image_width)

    if len(str(item.video_id)) > 5:
        md += "\nvideo_id: '" + item.video_id + "'"

    if len(str(item.presentation_url)) > 5:
        md += "\npresentation: '" + os.path.join(base_file_path, item.presentation_url) + "'"

    if len(str(item.poster_url)) > 5:
        md += "\nposter: '" + os.path.join(base_file_path, item.poster_url) + "'"

    if len(str(item.code_url)) > 5:
        md += "\ncode: '" + item.code_url + "'"
        md += "\ncodename: '" + item.code_name + "'"

    if len(str(item.data_url)) > 5:
        md += "\ndata: '" + str(item.data_url) + "'"
        md += "\ndataname: '" + str(item.data_name) + "'"

    if len(str(item.categories)) > 0:
        md += "\ncategories: "
        for c in item.categories.split(','):
            md += "\n  - " + cat_dict[c]

    md += "\ncitation: '" + html_escape(item.citation) + "'"

    md += "\nauthor_profile: true"
    
    md += "\n---"

    md_filename = os.path.basename(md_filename)

    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)
