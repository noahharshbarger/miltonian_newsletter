from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# Sample submission data
articles = [
    {
        "title": "Community Garden Opening",
        "content": "Join us for the grand opening of the new community garden this Saturday at 10 AM. There will be refreshments and gardening tips from local experts.",
        "author": "Jane Doe",
        "image": "images/photo1.jpg"
    }
]

events = [
    {
        "title": "Town Hall Meeting",
        "date": "Sept 20, 2025",
        "location": "City Hall",
        "description": "Discuss upcoming projects and community concerns with local officials. All residents are encouraged"
    },
    {
        "title": "Fall Festival",
        "date": "Sept 30, 2025",
        "location": "Central Park",
        "description": "Celebrate the season with food, music, and fun activities for all ages."
    }
]

photos = [
    {
        "url": "images/photo2.jpg",
        "caption": "Park Cleanup",
        "author": "John Smith"
    }
]

# Load template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('newsletter_template.html')

# Render HTML
html_out = template.render(
    articles=articles,
    events=events,
    photos=photos,
    page_number="1"
)

# Generate PDF
HTML(string=html_out).write_pdf("city_newsletter.pdf")

print("Newsletter generated: city_newsletter.pdf")