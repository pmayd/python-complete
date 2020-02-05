
def extract_toc_from_md(markdown: str) -> list:
    """Given a text in markdown syntax this function returns the toc
    
    Arguments:
        markdown {str} -- the text of the markdown file
    
    Returns:
        str -- the toc with appropriate level numbers
    """
    if markdown.find('#') == -1:
        return ""
    
    toc = []

    return toc


if __name__ == "__main__":
    with open(r'C:\Users\micha\work\git\python-complete\data\TEST.md', 'r', encoding='utf-8') as f:
        md = f.read()
    
    toc = extract_toc_from_md(md)
    print(toc)