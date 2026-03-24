from playwright.sync_api import sync_playwright
import json

def scrape_books():
    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # JS-heavy demo site
        page.goto("https://quotes.toscrape.com/")

        page.wait_for_selector(".product_pod")

        books = page.query_selector_all(".product_pod")

        for book in books:
            title = book.query_selector("h3 a").get_attribute("title")
            price = book.query_selector(".price_color").inner_text()
            availability = book.query_selector(".availability").inner_text().strip()

            data.append({
                "title": title,
                "price": price,
                "availability": availability
            })

        browser.close()

    with open("data/raw.json", "w") as f:
        json.dump(data, f, indent=4)

    return data


if __name__ == "__main__":
    scrape_books()
