from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader("Shraddha/templates")
)

template = env.get_template("proposal2.html")

data = {
    "client_name": "CODE ORBIT groups pvt. ltd.",
    "price": 75000,

    "can_meet": [
        "Website Design",
        "Software development",
        "Hosting",
        "Application development"
    ],

    "cannot_meet": [
        "Search engin optimaization"
    ]
}

rendered_html = template.render(**data)

with open(
    "Shraddha/output/proposal_rendered.html",
    "w",
    encoding="utf-8"
) as file:
    file.write(rendered_html)

print("Proposal Generated!")