# GoGetJob

This project is a simple content aggregator for job postings and opportunities, it is a web app that will serve as the user’s ideal tool to get recent job postings and opportunities based on their interests. Using Python Flask, sqlalchemy, Pandas, MechanicalSoup or alternatively Selenium and Beautiful Soup. A search keyword is entered into a web form, and is processed by a web scraper that returns a date stamped CSV file and also adds the results to the SQLite database.

This currently works with weworkremotely.com further modifications can extend this to researching and scraping from multiple job boards.

Entering the following into the job search form:
keyword = devops
Returns => devops job listings.

## Future Improvements

- User Accounts for personalized experiences, users can set preferences to recieve updates on new listings using job titles, keywords, location.
