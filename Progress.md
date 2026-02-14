# 08/02/26
# What you have done (if anything)
- Made a repository but don't have access to the classroom
- Used pdf-extractor-kit to extract text from pdfs 
- I used pdf-extractor-kit on two exam papers I found because I don't have access to the classroom and it worked
- Replicated the dashboard we made in class, but just made the pages they don't have any functionality yet

# What ideas are you considering (if anything).
- Plan to get the other exam papers and replicate what I have done with the two I had already completed.
- Then take a page at a time, so starting with introduction then search by topic etc. 
- I'm hoping to make progress every week on pages and look into adding more functionality

# What issues you have encountered. (if any)
- I clicked the button to get another invitation for GitHub classroom but no invitation has been sent in the past couple of days. 
- Other than that no other issues have been encountered yet. 




# 14/02/26
# What you have done (if anything)
- used PyMuPDF , and Tesseract to parse the PDFs properly, the pdf extractor kit did not work as I had hoped so I started all over again 
- create Data 01 Import.ipynb where i cleaned the PDFs so that Ill actually be able to use streamlit easier
    - Removing blank pages and very short pages
    - Removing formula sheets and cheat sheet pages
    - Fixing common OCR spelling errors
    - Extracting metadata (year, sitting, exam type)
    - Distinguishing between exam papers and marking schemes
    - Identifying question structure (Question, a), i), marks, etc.)
    - Tagging topics using keyword matching
    - Removing unnecessary newline characters
- Saved the cleaned dataset as a CSV file to use in Streamlit.


# What ideas are you considering (if anything).

- start working on EDA AND baseline model for the exam papers 
- start on streamlit dashboard

# What issues you have encountered. (if any)
- github classroom 
- trying to find the correct like setting for ocr to make sure it actually picked up the text that was alot of trial and error 
