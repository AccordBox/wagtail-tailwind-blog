import markdown


def render_markdown(value):
    html = markdown.markdown(
        value,
        extensions=[
            "extra",
            "mdx_math",
        ],
        output_format="html5",
    )
    return html
