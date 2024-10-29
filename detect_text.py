from PyPDF2 import PdfReader

def extract_text_with_packing_list(pdf_path):

    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)

        for page_number, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if text and "PACKING-LIST" in text.upper():  # Check for "PACKING-LIST"
                print(f"\n--- Page {page_number} ---")
                print(text) 

if __name__ == "__main__":
    pdf_path = "4.pdf"  # Replace with your PDF file path
    extract_text_with_packing_list(pdf_path)
