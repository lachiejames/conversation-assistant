from jinja2 import Environment, PackageLoader, select_autoescape


def get_template_env() -> Environment:
    return Environment(
        loader=PackageLoader(package_path="prompt_templates"),
        autoescape=select_autoescape(),
        keep_trailing_newline=True,
    )
