# License: MIT
# Copyright © 2023 Frequenz Energy-as-a-Service GmbH

"""Generate the code reference pages."""

from frequenz.repo.config import mkdocs

mkdocs.generate_python_api_pages("py", "python-reference")
mkdocs.generate_protobuf_api_pages()
