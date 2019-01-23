from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as req

def scrape():
    
     scrape_mars_dict = {}
     url = 'https://mars.nasa.gov/news/'

     response = req.get(url)

     soup = bs(response.text, 'html.parser')

     print(soup.prettify())

     results = soup.find("div", class_="features")

     article_title = results.find("div", class_="content_title").text
     asumm = results.find("div", class_="rollover_description").text
     print("Title: "+str(article_title))
     print("Summary: "+str(asumm))

     featured_image_url: "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA14924_ip.jpg"

     scrape_mars_dict['featured_image_url'] = featured_image_url

     twitter_url = "https://twitter.com/marswxreport?lang=en"
     twitter_response = req.get(twitter_url)
     twitter_bsoup = bs(twitter_response.text, "html.parser")

     print(soup.prettify())

     twitter_result = twitter_bsoup.find("div", class_="js-tweet-text-container")
     mars_weather = twitter_result.find("p", class_="js-tweet-text").text
     print(mars_weather)

     scrape_mars_dict['mars_weather'] = mars_weather

     mars_facts_url = "https://space-facts.com/mars/"
     result = pd.read_html(mars_facts_url)
     print(result)

     result_df = result[0]
     result_df.columns = ["Parameter", "Value"]
     result_df.set_index("Parameter", inplace=True)
     result_df

     result_df = result_df.to_html()

     result_df

     scrape_mars_dict['mars_facts'] = result_df

     hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

     # Valles Marineris Hemisphere Enhanced
     url1 = "https://mars.nasa.gov/system/resources/detail_files/6453_mars-globe-valles-marineris-enhanced-full2.jpg"
     # Cerberus Hemisphere Enhanced
     url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cerberus_Hemisphere_Enhanced.jpg/600px-Cerberus_Hemisphere_Enhanced.jpg"
     # Schiaparelli Hemisphere Enhanced
     url3 = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Schiaparelli_Hemisphere_Enhanced.jpg/600px-Schiaparelli_Hemisphere_Enhanced.jpg"
     # Syrtis Major Hemisphere Enhanced
     url4 = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/PlanetMars-SyrtisMajor-VikingOrbiter-1980.jpg/600px-PlanetMars-SyrtisMajor-VikingOrbiter-1980.jpg"

     scrape_mars_dict['hemisphere_1'] = url1
     scrape_mars_dict['hemisphere_2'] = url2
     scrape_mars_dict['hemisphere_3'] = url3
     scrape_mars_dict['hemisphere_4'] = url4


     return scrape_mars_dict