Web scraping is a data extraction method that collects data only from websites. 
It is often used for data mining and gathering valuable insights from large websites. 
Web scraping is also useful for personal use. 
Python includes a nice library called BeautifulSoup that enables web scraping.

# Required Modules:
1. The Requests module allows you to integrate your Python programs with web services.
2. The Beautiful Soup module is designed to make screen scraping a snap. 
    Using Python’s interactive console and these two libraries, 
    we’ll walk through how to assemble a web page and work with the textual information available on it.
3. The Pandas module is designed to provide high-performance data manipulation in Python. 
    It is used for data analysis that requires lots of processing, such as restructuring, 
    cleaning or merging, etc.

    pip install pandas

# Approach:
1. Initially, we are going to import our required libraries.
2. Then we take the URL stored in our list.
3. We will feed the URL to our soup object which will then extract relevant information from the given URL based on the class id we provide it.
    Store all the data in the Pandas Dataframe and save it to a CSV file.