from collections import defaultdict

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
    lines = md.splitlines()
        
    for line in lines:
        if line.lstrip().startswith('#'):
            level = line.count('#')
            header = line.lstrip('#' * level + ' ')

            if level == 1:
                toc.append([header])
            elif level > 1:
                last_entry = toc[-1]
                for _ in range(level - 2):
                    last_entry = last_entry[-1]
                last_entry.append([header])

    return toc

if __name__ == "__main__":
    with open(r'C:\Users\micha\work\git\python-complete\data\TEST.md', 'r', encoding='utf-8') as f:
        md = f.read()
    
    toc = extract_toc_from_md(md)
    print(toc)