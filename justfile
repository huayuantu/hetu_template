set dotenv-load
set positional-arguments

default:
    just -l

just-doc:
    open https://just.systems/man/zh/

# Install hasura-cli if not exists
install-hasura-cli:
    #!/bin/bash
    if ! [ -x "$(command -v hasura)" ]; then
        echo "'hasura' could not be found, auto installing..."
        curl -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh | bash
    fi

# Install Poetry if not exists
install-poetry:
    #!/bin/bash
    if ! [ -x "$(command -v poetry)" ]; then
        echo "'poetry' could not be found, auto installing..."
        curl -sSL https://install.python-poetry.org | python3 -
    fi

# Install backend python dependency
install-python-dependency:
    cd ./backend && poetry install

# Install Dependencies For Backend Development
install-dev: install-hasura-cli install-poetry install-python-dependency
