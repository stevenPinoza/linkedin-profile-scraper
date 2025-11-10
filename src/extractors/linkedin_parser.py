thonimport requests
from bs4 import BeautifulSoup

def parse_profile(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        profile_data = {
            "firstName": soup.find("span", {"class": "top-card-layout__first-name"}).text,
            "lastName": soup.find("span", {"class": "top-card-layout__last-name"}).text,
            "headline": soup.find("h1", {"class": "top-card-layout__headline"}).text,
            "locationName": soup.find("span", {"class": "top-card__location"}).text,
            "industryName": soup.find("span", {"class": "top-card__industry"}).text,
            "summary": soup.find("div", {"class": "summary-section__summary-text"}).text.strip(),
            "profile_id": url.split('/')[-2],
            "profilePictureUrl": soup.find("img", {"class": "profile-photo-edit__image"})["src"]
        }
        return profile_data
    except Exception as e:
        print(f"Error parsing profile {url}: {e}")
        return None