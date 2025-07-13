def search (ppp):
    from googlesearch import search
    query = ppp
    num_results = 5 # Number of results you want

    for result in search(query, num_results=num_results):
        print(result)


search (".....")
